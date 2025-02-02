# pyright: reportPrivateUsage=false

from __future__ import annotations

from typing import Collection, Generic, Iterable, Iterator, TypeVar, overload

from typing_extensions import Self

from .. import _types as _t
from ._module_misc import CDATA, QName

_T = TypeVar("_T")

class _Element:
    @overload
    def __getitem__(self, __x: int) -> Self: ...
    @overload
    def __getitem__(self, __x: slice) -> list[Self]: ...
    def __contains__(self, __o: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Self]: ...
    def find(self, path: _t._ElemPathArg) -> Self | None: ...
    @overload
    def get(self, key: _t._AttrName) -> str | None: ...
    @overload
    def get(self, key: _t._AttrName, default: _T) -> str | _T: ...
    @overload
    def iter(self, *tags: _t._TagSelector) -> Iterator[Self]: ...
    @overload
    def iter(
        self, *, tag: _t._TagSelector | Iterable[_t._TagSelector] | None = None
    ) -> Iterator[Self]: ...
    def iterancestors(
        self, *, tag: _t._TagSelector | Collection[_t._TagSelector] | None = None
    ) -> Iterator[Self]: ...
    @overload
    def itertext(self, *tags: _t._TagSelector, with_tail: bool = True) -> Iterator[str]: ...
    @overload
    def itertext(
        self,
        *,
        tag: _t._TagSelector | Collection[_t._TagSelector] | None = None,
        with_tail: bool = True,
    ) -> Iterator[str]: ...
    @property
    def tag(self) -> str: ...
    @property
    def tail(self) -> str | None: ...
    @tail.setter
    def tail(self, value: str | CDATA | None) -> None: ...
    @property
    def text(self) -> str | None: ...
    @text.setter
    def text(self, value: str | QName | CDATA | None) -> None: ...
    def xpath(
        self,
        _path: str,
        /,
    ) -> _t._XPathObject: ...

class _ElementTree(Generic[_t._ET_co]): ...

# Behaves like MutableMapping but deviates a lot in details
class _Attrib:
    def __bool__(self) -> bool: ...
    def __contains__(self, __o: object) -> bool: ...
    def __delitem__(self, __k: _t._AttrName) -> None: ...
    def __getitem__(self, __k: _t._AttrName) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, __k: _t._AttrName, __v: _t._AttrVal) -> None: ...
    @property
    def _element(self) -> _Element: ...
    def clear(self) -> None: ...
    def get(self, key: _t._AttrName, default: _T) -> str | _T: ...
    def has_key(self, key: _t._AttrName) -> bool: ...
    def items(self) -> list[tuple[str, str]]: ...
    def iteritems(self) -> Iterator[tuple[str, str]]: ...
    def iterkeys(self) -> Iterator[str]: ...
    def itervalues(self) -> Iterator[str]: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[str]: ...
