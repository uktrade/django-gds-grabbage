from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional

from django.forms.utils import RenderableMixin
from django.utils.safestring import mark_safe
from jinja2 import (
    ChoiceLoader,
    Environment,
    PackageLoader,
    PrefixLoader,
    select_autoescape,
)

Attributes = Dict[str, Any]


@dataclass(kw_only=True)
class GovUKComponent(RenderableMixin):
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None

    _jinja2_template: ClassVar[str]
    _macro_name: ClassVar[str]

    def build_jinja_template(self):
        return "".join(
            [
                "{%- from '",
                self._jinja2_template,
                "' import ",
                self._macro_name,
                " -%}",
                "{{ ",
                self._macro_name,
                "(data) }}",
            ]
        )

    def render(
        self,
        template_name=None,
        context=None,
        renderer=None,
        component_data=None,
    ):
        jinja_loader = ChoiceLoader(
            [
                PrefixLoader(
                    {"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}
                )
            ]
        )
        env = Environment(
            loader=jinja_loader,
            autoescape=select_autoescape(),
        )
        template = env.from_string(self.build_jinja_template())

        data = self.__dict__
        if component_data:
            data.update(component_data)

        return mark_safe(template.render(data=data))

    __str__ = render
    __html__ = render


@dataclass(kw_only=True)
class FieldsetLegend:
    text: str
    isPageHeading: bool
    classes: str


@dataclass(kw_only=True)
class TextAndHtml:
    text: Optional[str] = None
    html: Optional[str] = None


@dataclass(kw_only=True)
class FormGroup:
    classes: Optional[str] = None


"""
Accordion
"""


@dataclass(kw_only=True)
class AccordionItem:
    heading: Optional[TextAndHtml] = None
    summary: Optional[TextAndHtml] = None
    content: Optional[TextAndHtml] = None
    expanded: Optional[bool] = None


"""
Checkboxes
"""


@dataclass(kw_only=True)
class CheckboxesConditional:
    html: str


"""
Summary List
"""


@dataclass(kw_only=True)
class SummaryListRowsActionsItem:
    href: str
    text: Optional[str]
    html: Optional[str]
    visuallyHiddenText: Optional[str] = None
    classes: Optional[str] = None
    attributes: Optional[Attributes] = None


@dataclass(kw_only=True)
class SummaryListRowsKey(TextAndHtml):
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRowsValue(TextAndHtml):
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRowsActions:
    items: List[SummaryListRowsActionsItem]
    classes: Optional[str] = None


@dataclass(kw_only=True)
class SummaryListRow:
    classes: Optional[str] = None
    key: Optional[SummaryListRowsActions] = None
    value: Optional[SummaryListRowsValue] = None
    actions: Optional[SummaryListRowsActions] = None


SummaryListRows = List[SummaryListRow]
