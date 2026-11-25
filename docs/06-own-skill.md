> 🌍 Read this in: **English** | [Česky](06-own-skill.cs.md)

# 06 · Your own skill, and the team rollout

## When a task deserves a skill

You did it three times, you explained the same rules each time, and the result depends on
those rules. Examples from sales: follow-up after a first call, a reference one-pager, a
weekly pipeline note, a reply to a tender clarification.

## Anatomy

```
my-skill/
  SKILL.md          # frontmatter: name, description; then the instructions
  references/       # long material Claude reads only when needed
  assets/           # logos, templates
```

The **description** decides when the skill is used: write what it does and the words people
actually say ("follow-up", "zápis ze schůzky"). The **body** is a checklist a new colleague
could follow: inputs, steps, output format, a final check.

## Creating one in Claude

Ask Claude to create the skill with you (the built-in `skill-creator`, or `create-cowork-plugin`
for a whole plugin). Give it a real example of a good output and the rules you keep repeating.
Test it on a second example; fix the instructions, not the output.

## Rolling out to the team

| Step | Who | Where |
|---|---|---|
| Change the skill in `plugins/quanti-sales/`, bump `version` in `plugin.json` | Skill owner | This repo |
| `scripts/build-plugin.sh` → `dist/quanti-sales.zip` | Skill owner | Terminal |
| Upload; same name overwrites the old version | Org owner | Organization settings → Plugins & skills → Add → Upload a plugin |
| Set *Installed by default* (or *Required*) for the sales group | Org owner | The plugin's install setting |

Alternative: add this repository as a plugin marketplace (it has
`.claude-plugin/marketplace.json`); then updates arrive with each push. A private repository
needs GitHub access for every user, so the zip upload is simpler for a sales team.
