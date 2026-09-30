import sys
from typing import Any, Dict, Type, Union

class ValidationError(TypeError):
    """Raised when runtime types or invariants violate schema contracts."""
    pass

class Field:
    """Implements the Descriptor Protocol to intercept attribute access and mutate state."""
    def __init__(self, expected_type: Type, default: Any = None):
        self.expected_type = expected_type
        self.default = default
        self.storage_name = None  # Injected dynamically by the metaclass

    def __get__(self, instance: Any, owner: Type) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.storage_name, self.default)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, self.expected_type):
            raise ValidationError(
                f"Invalid assignment! Type '{type(value).__name__}' "
                f"cannot be assigned to field '{self.storage_name}' (Expected {self.expected_type.__name__})."
            )
        instance.__dict__[self.storage_name] = value


class MetaclassRegistry(type):
    """
    The brain of the runtime architecture. Intercepts class definition,
    rewrites namespaces, processes descriptors, and dynamically hooks slots.
    """
    def __new__(mcs, name: str, bases: tuple, namespaces: Dict[str, Any]) -> Type:
        # Prevent base class validation interceptor setup
        if bases == (object,) or not bases:
            return super().__new__(mcs, name, bases, namespaces)

        fields = {}
        # Scrape data fields and bind structural storage locations dynamically
        for key, value in list(namespaces.items()):
            if isinstance(value, Field):
                value.storage_name = f"_{key}"
                fields[key] = value
                # Relocate properties to avoid collision and enforce the protocol
                namespaces[f"_{key}"] = value.default
                
        namespaces["_fields_map"] = fields

        # Dynamically inject structural framework requirements into the generated class
        def init_injector(self, **kwargs: Any) -> None:
            for field_name, field_obj in self._fields_map.items():
                val = kwargs.get(field_name, field_obj.default)
                setattr(self, field_name, val)
                
        namespaces["__init__"] = init_injector
        
        # Build and return the sealed class type definition
        new_class = super().__new__(mcs, name, bases, namespaces)
        return new_class


class StrictModel(metaclass=MetaclassRegistry):
    """Base class exposing the metaclass architecture to standard definitions."""
    def __setattr__(self, name: str, value: Any) -> None:
        # Enforce structural integrity: prevent adding arbitrary untyped variables
        if name not in self._fields_map and not name.startswith('_'):
            raise ValidationError(f"Enforced Schema Contract: Cannot append unmapped attribute '{name}'.")
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in self._fields_map)
        return f"<{self.__class__.__name__} ({attrs})>"


# ==========================================
# VERIFICATION AND EXECUTION
# ==========================================
if __name__ == "__main__":
    # Define a clean, declarative data structure
    class QuantitativeAsset(StrictModel):
        ticker = Field(str, default="UNKNOWN")
        allocation_pct = Field(float, default=0.0)
        units = Field(int, default=0)

    # 1. Correct Execution
    try:
        portfolio_item = QuantitativeAsset(ticker="AAPL", allocation_pct=42.5, units=100)
        print("Successfully Initialized:", portfolio_item)
        
        # Updating safely within boundaries
        portfolio_item.units = 150
        print("Updated Units:", portfolio_item)
    except ValidationError as e:
        print("Unexpected Error:", e)

    # 2. Type Violations (Handled and Rejected at Runtime)
    print("\n--- Testing Runtime Type Guardrails ---")
    try:
        portfolio_item.allocation_pct = "High"  # Throws exception (string given instead of float)
    except ValidationError as err:
        print("Intercepted Violation:", err)

    # 3. Structural Adherence Violations (Handled and Rejected)
    try:
        portfolio_item.unauthorized_metadata = "Malicious Injection"  # Rejects new field bindings
    except ValidationError as err:
        print("Intercepted Schema Breaker:", err)
