from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata

import pandas as pd
from mendeleev.fetch import fetch_table


class TableDocDirective(SphinxDirective):
    """A directive to say hello!"""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        # paragraph_node = nodes.paragraph(text=f'hello {self.arguments[0]}!')

        class_name = self.arguments[0]

        columns = [
            "attribute_name",
            "description",
            "unit",
            "value_origin",
            "citation_keys",
        ]

        table = fetch_table("propertymetadata")
        table = table.loc[table["class_name"] == class_name, columns]
        table_node = self.pandas_to_docutils_table(table, "citation_keys")
        return [table_node]

    def pandas_to_docutils_table(
        self, df: pd.DataFrame, citation_column: str
    ) -> nodes.table:
        """
        Convert a pandas DataFrame into a docutils.table node.

        Parameters:
        - df (pd.DataFrame): The DataFrame to convert.

        Returns:
        - nodes.table: A docutils table node representing the DataFrame.
        """
        table = nodes.table()

        # Define the table structure
        tgroup = nodes.tgroup(cols=len(df.columns))
        table += tgroup

        # Define columns
        for _ in df.columns:
            tgroup += nodes.colspec(colwidth=1)

        # Add header row
        thead = nodes.thead()
        tgroup += thead
        header_row = nodes.row()
        thead += header_row
        for column_name in df.columns:
            entry = nodes.entry()
            entry += nodes.paragraph(text=str(column_name))
            header_row += entry

        # Add data rows
        tbody = nodes.tbody()
        tgroup += tbody
        for _, row in df.iterrows():
            body_row = nodes.row()
            tbody += body_row

            for column_name, cell_value in row.items():
                entry = nodes.entry()

                # Check if the column is the one to render with :cite:
                if column_name == citation_column:
                    paragraph = nodes.paragraph()
                    if cell_value is None:
                        paragraph += nodes.Text("")
                    else:
                        refname = nodes.fully_normalize_name(cell_value)

                        # add citation
                        citation = nodes.citation()
                        citation["names"].append(refname)
                        citation += nodes.label("", refname)
                        citation += nodes.paragraph(text=str(cell_value))
                        self.state.document.note_citation(citation)
                        self.state.document.note_explicit_target(citation, citation)

                        # add citation reference
                        refnode = nodes.citation_reference(refname=refname)
                        refnode += nodes.Text(f"{cell_value}")
                        self.state.document.note_citation_ref(refnode)
                        paragraph += refnode

                    # for citation_key in str(cell_value).split(","):
                    #     citation_key = citation_key.strip()
                    #     refnode = nodes.citation_reference(refname=citation_key)
                    #     refnode += nodes.Text(f"{citation_key}")
                    #     paragraph += refnode
                    #     self.state.document.note_citation_ref(refnode)

                elif column_name == "attribute_name":
                    paragraph = nodes.paragraph()
                    if cell_value is None:
                        paragraph += nodes.Text("")
                    else:
                        paragraph += nodes.strong(text=str(cell_value))
                else:
                    paragraph = nodes.paragraph(text=str(cell_value))

                entry += paragraph
                body_row += entry

        return table


def setup(app: Sphinx) -> ExtensionMetadata:
    # app.add_role('hello', HelloRole())
    app.add_directive("ormtableproperties", TableDocDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
