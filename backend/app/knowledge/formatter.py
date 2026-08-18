from app.knowledge.models import RepositoryKnowledge


class KnowledgeFormatter:

    MAX_TREE_CHARS = 6000
    MAX_SOURCE_FILES = 6
    MAX_SOURCE_CHARS_PER_FILE = 3000
    MAX_TOTAL_SOURCE_CHARS = 16000

    def format(
        self,
        knowledge: RepositoryKnowledge,
    ) -> str:

        lines = []

        # =========================================
        # Repository Information
        # =========================================

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

            for dependency in knowledge.dependencies[:100]:
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

        # =========================================
        # Repository Tree
        # =========================================

        if knowledge.tree:

            tree = knowledge.tree

            if len(tree) > self.MAX_TREE_CHARS:
                tree = (
                    tree[:self.MAX_TREE_CHARS]
                    + "\n...\n"
                    + "[Repository tree truncated]"
                )

            lines.extend([
                "## Repository Tree",
                "",
                "```text",
                tree,
                "```",
                "",
            ])

        # =========================================
        # Repository Statistics
        # =========================================

        stats = knowledge.statistics

        lines.extend([
            "## Repository Statistics",
            "",
            f"- Files: {stats.total_files}",
            f"- Classes: {stats.total_classes}",
            f"- Functions: {stats.total_functions}",
            "",
        ])

        # =========================================
        # Module Metadata
        # =========================================

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

                for imp in module.imports[:30]:
                    lines.append(f"- {imp}")

                lines.append("")

            if module.classes:

                lines.append("Classes:")

                for cls in module.classes[:30]:
                    lines.append(f"- {cls}")

                lines.append("")

            if module.functions:

                lines.append("Functions:")

                for fn in module.functions[:50]:
                    lines.append(f"- {fn}")

                lines.append("")

        # =========================================
        # Select Important Source Files
        # =========================================

        important_modules = []

        for module in knowledge.modules:

            if not module.source:
                continue

            path = module.path.lower()

            score = 0

            # Entry points / orchestration
            if any(
                name in path
                for name in [
                    "main.py",
                    "app.py",
                    "__main__.py",
                    "engine.py",
                    "server.py",
                ]
            ):
                score += 10

            # API / routing
            if any(
                name in path
                for name in [
                    "router",
                    "route",
                    "api",
                    "endpoint",
                ]
            ):
                score += 7

            # AI / agent / workflow modules
            if any(
                name in path
                for name in [
                    "agent",
                    "workflow",
                    "chain",
                    "node",
                    "model",
                ]
            ):
                score += 6

            # Database / storage
            if any(
                name in path
                for name in [
                    "database",
                    "db",
                    "repository",
                    "storage",
                    "vector",
                ]
            ):
                score += 5

            # Classes and functions indicate implementation value
            if module.classes:
                score += 2

            if module.functions:
                score += 2

            # Import count gives architectural signal
            if len(module.imports) >= 3:
                score += 1

            important_modules.append(
                (score, module)
            )

        important_modules.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        # =========================================
        # Important Source Code
        # =========================================

        lines.extend([
            "## Important Source Files",
            "",
            "The following source files were selected because "
            "they are most relevant to understanding the "
            "repository architecture and execution flow.",
            "",
        ])

        total_source_chars = 0

        for _, module in important_modules[
            :self.MAX_SOURCE_FILES
        ]:

            if (
                total_source_chars
                >= self.MAX_TOTAL_SOURCE_CHARS
            ):
                break

            source = module.source

            remaining = (
                self.MAX_TOTAL_SOURCE_CHARS
                - total_source_chars
            )

            limit = min(
                self.MAX_SOURCE_CHARS_PER_FILE,
                remaining,
            )

            if len(source) > limit:

                source = (
                    source[:limit]
                    + "\n\n"
                    + "[Source truncated for context efficiency]"
                )

            total_source_chars += len(source)

            # Try to use the actual language
            language = (
                module.language.lower()
                if module.language
                else "text"
            )

            language_map = {
                "python": "python",
                "javascript": "javascript",
                "typescript": "typescript",
                "java": "java",
                "cpp": "cpp",
                "c++": "cpp",
                "go": "go",
                "rust": "rust",
            }

            fence_language = language_map.get(
                language,
                "text",
            )

            lines.extend([
                f"### {module.path}",
                "",
                f"Language: {module.language}",
                "",
                f"```{fence_language}",
                source,
                "```",
                "",
            ])

        # =========================================
        # Final Context
        # =========================================

        return "\n".join(lines)