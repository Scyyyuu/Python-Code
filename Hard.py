import sys
from typing import Any, Dict, Type, Union

class ValidationError(TypeError):
    pass

class Field:

    def __init__(self, expected_type: Type, default: Any = None):
        self.expected_type = expected_type
        self.default = default
        self.storage_name = None  

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
    def __new__(mcs, name: str, bases: tuple, namespaces: Dict[str, Any]) -> Type:
        if bases == (object,) or not bases:
            return super().__new__(mcs, name, bases, namespaces)

        fields = {}
        for key, value in list(namespaces.items()):
            if isinstance(value, Field):
                value.storage_name = f"_{key}"
                fields[key] = value
                namespaces[f"_{key}"] = value.default
                
        namespaces["_fields_map"] = fields


        def init_injector(self, **kwargs: Any) -> None:
            for field_name, field_obj in self._fields_map.items():
                val = kwargs.get(field_name, field_obj.default)
                setattr(self, field_name, val)
                
        namespaces["__init__"] = init_injector
        

        new_class = super().__new__(mcs, name, bases, namespaces)
        return new_class


class StrictModel(metaclass=MetaclassRegistry):
    def __setattr__(self, name: str, value: Any) -> None:
 
        if name not in self._fields_map and not name.startswith('_'):
            raise ValidationError(f"Enforced Schema Contract: Cannot append unmapped attribute '{name}'.")
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in self._fields_map)
        return f"<{self.__class__.__name__} ({attrs})>"



if __name__ == "__main__":
    class QuantitativeAsset(StrictModel):
        ticker = Field(str, default="UNKNOWN")
        allocation_pct = Field(float, default=0.0)
        units = Field(int, default=0)


    try:
        portfolio_item = QuantitativeAsset(ticker="AAPL", allocation_pct=42.5, units=100)
        print("Successfully Initialized:", portfolio_item)
        

        portfolio_item.units = 150
        print("Updated Units:", portfolio_item)
    except ValidationError as e:
        print("Unexpected Error:", e)


    print("\n--- Testing Runtime Type Guardrails ---")
    try:
        portfolio_item.allocation_pct = "High"  
    except ValidationError as err:
        print("Intercepted Violation:", err)


    try:
        portfolio_item.unauthorized_metadata = "Malicious Injection"  # Rejects new field bindings
        print("Intercepted Schema Breaker:", err)
