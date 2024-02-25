import pytest

from zen.utils.struct import *


# Test for nullable_struct
class TestNullableStruct:
    @pytest.fixture
    def NullablePerson(self):
        @nullable_struct
        class Person:
            name: str
            age: int

        return Person

    def test_nullable_struct_init(self, NullablePerson):
        person = NullablePerson(name="Alice", age=30)
        assert person.name == "Alice"
        assert person.age == 30

    def test_nullable_struct_defaults(self, NullablePerson):
        person = NullablePerson(name="Bob")
        assert person.name == "Bob"
        assert person.age is None

    def test_nullable_struct_repr(self, NullablePerson):
        person = NullablePerson(name="Charlie", age=25)
        assert repr(person) == "Person(name='Charlie', age=25)"

    def test_nullable_struct_eq(self, NullablePerson):
        person1 = NullablePerson(name="Diana", age=35)
        person2 = NullablePerson(name="Diana", age=35)
        assert person1 == person2


# Test for struct
class TestStruct:
    @pytest.fixture
    def Person(self):
        @struct(check_type=True)
        class Person:
            name: str
            age: int

        return Person

    def test_struct_init(self, Person):
        person = Person(name="Eve", age=40)
        assert person.name == "Eve"
        assert person.age == 40

    def test_struct_type_check(self, Person):
        with pytest.raises(TypeError):
            Person(name="Frank", age="45")

    def test_struct_repr(self, Person):
        person = Person(name="Grace", age=45)
        assert repr(person) == "Person(name='Grace', age=45)"

    def test_struct_eq(self, Person):
        person1 = Person(name="Hannah", age=50)
        person2 = Person(name="Hannah", age=50)
        assert person1 == person2
