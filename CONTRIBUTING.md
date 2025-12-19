# Contributing to Discord.py Bot Template

Thanks for your interest in contributing!

This project aims to help beginners learn Discord bot development, so contributions that make the template more accessible and useful are especially welcome.

## How to Contribute

### Reporting Bugs
- Check if the bug has already been reported in [Issues](https://github.com/egeyardimci/Discord-Py-Bot-Template/issues)
- If not, create a new issue with:
  - A clear title and description
  - Steps to reproduce the bug
  - Expected vs actual behavior
  - Your Python and discord.py versions

### Suggesting Features
- Open an issue with the `enhancement` label
- Describe the feature and why it would be useful
- If possible, provide examples of how it would work

### Submitting Code

1. **Fork the repository**

2. **Create a branch** (see [Branch Naming Convention](#branch-naming-convention) below)
   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow existing code style and structure
   - Add comments for complex logic
   - Keep it beginner-friendly!

4. **Test your changes**
   - Make sure the bot runs without errors
   - Test your new features/commands

5. **Commit your changes** (see [Commit Message Convention](#commit-message-convention) below)
   ```bash
   git commit -m "feat: add user authentication command"
   ```

6. **Push to your fork**
   ```bash
   git push origin feat/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues

## What We're Looking For

**Good Contributions:**
- New example commands that demonstrate Discord.py features
- Bug fixes and improvements
- Better error handling
- Documentation improvements
- Code simplification for beginners

**Please Avoid:**
- Breaking changes without discussion
- Overly complex code that's hard for beginners to understand
- Dependencies that aren't necessary
- Removing existing functionality

## Code Style

- Use clear, descriptive variable names
- Add comments explaining what code does (remember, beginners will read this!)
- Follow PEP 8 style guidelines
- Keep functions simple and focused

## Commit Message Convention

This project follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Changes that don't affect code meaning (formatting, whitespace) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `build` | Changes to build system or dependencies |
| `ci` | Changes to CI configuration files and scripts |
| `chore` | Other changes that don't modify src or test files |

### Examples

```bash
feat: add new /ban command
fix: resolve memory leak in event handler
docs: update README with setup instructions
feat(commands): add user profile lookup
fix!: change API response format
```

### Breaking Changes

Indicate breaking changes by:
- Adding `!` after the type/scope: `feat!: change command prefix`
- Adding a `BREAKING CHANGE:` footer in the commit body

## Branch Naming Convention

This project follows the [Conventional Branch](https://conventional-branch.github.io/) naming convention.

### Format

```
<type>/<description>
```

### Branch Types

| Prefix | Purpose | Example |
|--------|---------|---------|
| `feat/` | New features | `feat/add-moderation-commands` |
| `fix/` | Bug fixes | `fix/reaction-handler-crash` |
| `hotfix/` | Urgent production fixes | `hotfix/security-vulnerability` |
| `docs/` | Documentation updates | `docs/update-readme` |
| `refactor/` | Code refactoring | `refactor/simplify-event-handlers` |
| `test/` | Test additions/changes | `test/add-command-tests` |
| `chore/` | Maintenance tasks | `chore/update-dependencies` |
| `release/` | Release preparation | `release/v1.2.0` |

### Naming Rules

- Use **lowercase letters**, numbers, and hyphens only
- Use hyphens to separate words: `feat/add-new-command`
- Keep descriptions concise but descriptive
- Include issue numbers when applicable: `feat/issue-123-add-logging`
- No consecutive, leading, or trailing hyphens

### Examples

```bash
git checkout -b feat/add-music-player
git checkout -b fix/command-cooldown-bug
git checkout -b docs/api-documentation
git checkout -b chore/upgrade-discord-py
```

## Questions?

Feel free to open an issue if you have questions about contributing!

---

By contributing, you agree that your contributions will be licensed under the MIT License.
