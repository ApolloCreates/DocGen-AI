from app.knowledge.models import RepositoryKnowledge


class KnowledgeFormatter:

    def format(
        self,
        knowledge: RepositoryKnowledge,
    ) -> str:

        lines = []

        lines.extend([
            "# Repository Information",
            "",
            f"Project: {knowledge.project_name}",
            "",
        ])

        if knowledge.languages:
            lines.append("## Languages")

            for language in knowledge.languages:
                lines.append(f"- {language}")

            lines.append("")

        if knowledge.frameworks:
            lines.append("## Frameworks")

            for framework in knowledge.frameworks:
                lines.append(f"- {framework}")

            lines.append("")

        if knowledge.dependencies:
            lines.append("## Dependencies")

            for dependency in knowledge.dependencies:
                lines.append(f"- {dependency}")

            lines.append("")

        if knowledge.package_manager:
            lines.extend([
                "## Package Manager",
                "",
                knowledge.package_manager,
                "",
            ])

        if knowledge.entry_points:
            lines.append("## Entry Points")

            for entry in knowledge.entry_points:
                lines.append(f"- {entry}")

            lines.append("")

        if knowledge.config_files:
            lines.append("## Configuration Files")

            for config in knowledge.config_files:
                lines.append(f"- {config}")

            lines.append("")

        if knowledge.tree:
            lines.extend([
                "## Repository Tree",
                "",
                "```text",
                knowledge.tree,
                "```",
                "",
            ])

        stats = knowledge.statistics

        lines.extend([
            "## Repository Statistics",
            "",
            f"- Files: {stats.total_files}",
            f"- Classes: {stats.total_classes}",
            f"- Functions: {stats.total_functions}",
            "",
        ])

        lines.extend([
            "## Modules",
            "",
        ])

        for module in knowledge.modules:

            lines.extend([
                f"### {module.path}",
                "",
                f"Language: {module.language}",
                "",
            ])

            if module.imports:
                lines.append("Imports:")

                for imp in module.imports:
                    lines.append(f"- {imp}")

                lines.append("")

            if module.classes:
                lines.append("Classes:")

                for cls in module.classes:
                    lines.append(f"- {cls}")

                lines.append("")

            if module.functions:
                lines.append("Functions:")

                for fn in module.functions:
                    lines.append(f"- {fn}")

                lines.append("")

        # =========================================
        # Important Source Code
        # =========================================

        important_modules = []

        for module in knowledge.modules:

            if not module.source:
                continue

            path = module.path.lower()

            score = 0

            if any(
                name in path
                for name in [
                    "main.py",
                    "app.py",
                    "engine.py",
                    "server.py",
                    "router.py",
                    "api",
                ]
            ):
                score += 5

            if module.classes:
                score += 2

            if module.functions:
                score += 2

            if len(module.imports) >= 3:
                score += 1

            important_modules.append(
                (score, module)
            )

        important_modules.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        lines.extend([
            "## Important Source Files",
            "",
        ])

        for _, module in important_modules[:8]:

            lines.extend([
                f"### {module.path}",
                "",
                "```python",
                module.source,
                "```",
                "",
            ])

        return "\n".join(lines)