from app.knowledge.models import RepositoryKnowledge


class KnowledgeFormatter:

    def format(self, knowledge: RepositoryKnowledge) -> str:

        lines = []

        # ---------------------------------
        # Repository
        # ---------------------------------

        lines.append(
            f"Project: {knowledge.project_name}"
        )

        lines.append("")

        # ---------------------------------
        # Languages
        # ---------------------------------

        if knowledge.languages:

            lines.append(
                "Languages:"
            )

            for language in knowledge.languages:

                lines.append(
                    f"- {language}"
                )

            lines.append("")

        # ---------------------------------
        # Frameworks
        # ---------------------------------

        if knowledge.frameworks:

            lines.append(
                "Frameworks:"
            )

            for framework in knowledge.frameworks:

                lines.append(
                    f"- {framework}"
                )

            lines.append("")
            
        if knowledge.tree:

            lines.extend([
                "Repository Tree:",
                "",
                "```text",
                knowledge.tree,
                "```",
                "",
            ])

        # ---------------------------------
        # Statistics
        # ---------------------------------

        stats = knowledge.statistics

        lines.extend([

            "Repository Statistics:",

            f"- Files: {stats.total_files}",

            f"- Classes: {stats.total_classes}",

            f"- Functions: {stats.total_functions}",

            ""

        ])

        # ---------------------------------
        # Modules
        # ---------------------------------

        lines.append("Modules:")

        lines.append("")

        for module in knowledge.modules:

            lines.append(
                f"### {module.path}"
            )

            if module.classes:

                lines.append(
                    "Classes:"
                )

                for cls in module.classes:

                    lines.append(
                        f"- {cls}"
                    )

            if module.functions:

                lines.append(
                    "Functions:"
                )

                for fn in module.functions:

                    lines.append(
                        f"- {fn}"
                    )

            if module.imports:

                lines.append(
                    "Imports:"
                )

                for imp in module.imports:

                    lines.append(
                        f"- {imp}"
                    )

            lines.append("")

        return "\n".join(lines)