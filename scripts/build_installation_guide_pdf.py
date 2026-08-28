#!/usr/bin/env python3
"""Build the concise Research-Agent installation guide PDF and render previews."""

from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2B6CB0")
TEAL = colors.HexColor("#137C8B")
PALE_BLUE = colors.HexColor("#EEF5FB")
PALE_TEAL = colors.HexColor("#EAF7F6")
PALE_GRAY = colors.HexColor("#F5F7FA")
MID_GRAY = colors.HexColor("#667085")
LINE = colors.HexColor("#D0D5DD")
INK = colors.HexColor("#1D2939")
WHITE = colors.white
GREEN = colors.HexColor("#027A48")

PAGE_W, PAGE_H = letter
MARGIN_X = 0.62 * inch
MARGIN_TOP = 0.70 * inch
MARGIN_BOTTOM = 0.56 * inch
CONTENT_W = PAGE_W - 2 * MARGIN_X


def styles():
    s = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle(
            "cover_title", parent=s["Title"], fontName="Helvetica-Bold",
            fontSize=27, leading=31, textColor=NAVY, alignment=TA_LEFT, spaceAfter=10,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", parent=s["BodyText"], fontName="Helvetica",
            fontSize=12.5, leading=18, textColor=MID_GRAY, spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "h1", parent=s["Heading1"], fontName="Helvetica-Bold",
            fontSize=17, leading=21, textColor=NAVY, spaceBefore=2, spaceAfter=9,
        ),
        "h2": ParagraphStyle(
            "h2", parent=s["Heading2"], fontName="Helvetica-Bold",
            fontSize=11.5, leading=14, textColor=BLUE, spaceBefore=7, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "body", parent=s["BodyText"], fontName="Helvetica",
            fontSize=9.35, leading=13.2, textColor=INK, spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "small", parent=s["BodyText"], fontName="Helvetica",
            fontSize=8.1, leading=11.2, textColor=MID_GRAY,
        ),
        "code": ParagraphStyle(
            "code", parent=s["Code"], fontName="Courier",
            fontSize=7.7, leading=10.4, textColor=INK, leftIndent=0, rightIndent=0,
        ),
        "step": ParagraphStyle(
            "step", parent=s["BodyText"], fontName="Helvetica-Bold",
            fontSize=10.2, leading=13.4, textColor=NAVY,
        ),
        "table": ParagraphStyle(
            "table", parent=s["BodyText"], fontName="Helvetica",
            fontSize=8.2, leading=10.8, textColor=INK,
        ),
        "table_b": ParagraphStyle(
            "table_b", parent=s["BodyText"], fontName="Helvetica-Bold",
            fontSize=8.2, leading=10.8, textColor=NAVY,
        ),
        "footer": ParagraphStyle(
            "footer", parent=s["BodyText"], fontName="Helvetica",
            fontSize=7.2, leading=9, textColor=MID_GRAY, alignment=TA_CENTER,
        ),
    }


ST = styles()


def p(text, style="body"):
    return Paragraph(text, ST[style])


def code_box(text: str):
    lines = text.strip("\n").splitlines()
    content = "<br/>".join(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") or " " for line in lines)
    t = Table([[Paragraph(content, ST["code"])]], colWidths=[CONTENT_W - 0.22 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE_GRAY),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


def callout(title: str, body: str, tone="blue"):
    bg = PALE_BLUE if tone == "blue" else PALE_TEAL
    accent = BLUE if tone == "blue" else TEAL
    cell = [p(title, "table_b"), Spacer(1, 3), p(body, "table")]
    t = Table([[cell]], colWidths=[CONTENT_W - 0.10 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 4, accent),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9E2EC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def step_table(rows):
    data = []
    for n, title, detail in rows:
        badge = Paragraph(f"<b>{n}</b>", ParagraphStyle("badge", parent=ST["table_b"], textColor=WHITE, alignment=TA_CENTER))
        data.append([badge, p(title, "table_b"), p(detail, "table")])
    t = Table(data, colWidths=[0.34 * inch, 1.42 * inch, CONTENT_W - 1.76 * inch], repeatRows=0)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), BLUE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (1, 0), (-1, -2), 0.4, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


def architecture_table():
    data = [
        [p("RESEARCH-AGENT SOURCE", "table_b"), p("CHATGPT", "table_b"), p("YOUR GITHUB REPO", "table_b")],
        [p("RESEARCH_AGENT.md<br/>Skill source<br/>release tooling", "table"), p("persistent Agent instructions<br/>installed skill.zip packages", "table"), p("AGENTS.md<br/>roadmap + Tasks<br/>evidence + history", "table")],
        [p("Reusable behavior", "small"), p("Runtime tooling", "small"), p("Project authority + state", "small")],
    ]
    t = Table(data, colWidths=[CONTENT_W / 3] * 3)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 1), (0, 1), PALE_BLUE),
        ("BACKGROUND", (1, 1), (1, 1), PALE_TEAL),
        ("BACKGROUND", (2, 1), (2, 1), colors.HexColor("#FFF7E8")),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def page_header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_X, PAGE_H - 0.39 * inch, PAGE_W - MARGIN_X, PAGE_H - 0.39 * inch)
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.setFillColor(NAVY)
        canvas.drawString(MARGIN_X, PAGE_H - 0.29 * inch, "RESEARCH-AGENT INSTALLATION GUIDE")
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MID_GRAY)
    footer = f"AidanRDonahue/Research-Agent  |  v0.1.0 architecture  |  page {doc.page}"
    w = stringWidth(footer, "Helvetica", 7.2)
    canvas.drawString((PAGE_W - w) / 2, 0.28 * inch, footer)
    canvas.restoreState()


def build_pdf(output: Path):
    frame = Frame(MARGIN_X, MARGIN_BOTTOM, CONTENT_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id="normal", showBoundary=0)
    doc = BaseDocTemplate(
        str(output), pagesize=letter, leftMargin=MARGIN_X, rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title="Research-Agent Installation Guide",
        author="AidanRDonahue/Research-Agent",
        subject="Install Research-Agent and Skills for a GitHub research repository",
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=page_header_footer)])

    story = []

    # Page 1 - Cover + mental model
    story += [
        Spacer(1, 0.23 * inch),
        p("Research-Agent", "cover_title"),
        p("Installation Guide for GitHub Research Repositories", "cover_title"),
        p("Set up a research GPT, install reusable Skills, bootstrap a GitHub repository, and keep the toolchain versioned without mixing project state with reusable workflow code.", "cover_sub"),
        Spacer(1, 0.08 * inch),
        architecture_table(),
        Spacer(1, 0.18 * inch),
        callout("The rule to remember", "The Agent and Skills normally live in ChatGPT. Your GitHub repository stores project-local rules and durable research state. Do not copy the Skill source into every project unless you deliberately want a vendored snapshot.", "teal"),
        Spacer(1, 0.18 * inch),
        p("What this guide covers", "h2"),
        step_table([
            ("1", "Prepare", "Connect ChatGPT to the GitHub repository and choose one Research-Agent version."),
            ("2", "Install", "Configure RESEARCH_AGENT.md and install each Skill independently as skill.zip."),
            ("3", "Bootstrap", "Ask bootstrap-research-project to create the local research system."),
            ("4", "Research", "Work in bounded task conversations; invoke standardized procedures in natural language."),
            ("5", "Upgrade", "Test new Research-Agent releases and update the project lock intentionally."),
        ]),
        Spacer(1, 0.15 * inch),
        p("Prerequisites: a GitHub repository, ChatGPT with GitHub access, and permission to install/configure the Research-Agent tooling you intend to use.", "small"),
        PageBreak(),
    ]

    # Page 2 - Installation
    story += [
        p("1. Install the Agent and Skills", "h1"),
        p("Choose one Research-Agent release or exact source commit. Keep the persistent Agent instructions and all installed Skills from that same version so the runtime is reproducible.", "body"),
        p("A. Connect the research repository", "h2"),
        p("Create or choose the GitHub repository that will hold your research. Connect ChatGPT to GitHub and grant that repository read access, plus write access if you want the Agent to publish branches, task files, evidence, or pull requests.", "body"),
        p("B. Configure collaborator behavior", "h2"),
        p("Use <b>RESEARCH_AGENT.md</b> from the chosen Research-Agent version as the persistent instructions for the GPT/agent that conducts research. Do not use the Research-Agent source repository's root AGENTS.md as the research prompt; your project gets its own local AGENTS.md during bootstrap.", "body"),
        p("C. Install the core Skills", "h2"),
        p("For the complete workflow, install these independent packages in ChatGPT:", "body"),
        Table([
            [p("bootstrap-research-project", "table_b"), p("define-research-task", "table_b")],
            [p("transcribe-research-evidence", "table"), p("review-mathematical-result", "table")],
            [p("restructure-research-roadmap", "table"), p("complete-research-task", "table")],
            [p("validate-research-project", "table"), p("synthesize-research-project", "table")],
        ], colWidths=[CONTENT_W / 2] * 2, style=TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
            ("BACKGROUND", (0, 0), (-1, 0), PALE_BLUE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ])),
        Spacer(1, 0.12 * inch),
        callout("Each Skill is separate", "Install each <skill-name>/skill.zip independently. A Research-Agent release bundle may contain many Skill archives for transport, but the outer bundle is not itself a Skill.", "blue"),
        p("D. If no release bundle is available", "h2"),
        code_box("""git clone https://github.com/AidanRDonahue/Research-Agent.git
cd Research-Agent
git checkout <EXACT-COMMIT-OR-TAG>
python scripts/package_skills.py --output dist"""),
        Spacer(1, 0.10 * inch),
        p("Install the individual packages under <b>dist/&lt;skill-name&gt;/skill.zip</b>. Keep <b>dist/research-agent-distribution.json</b>; it records the exact version and source commit used to build the packages.", "body"),
        PageBreak(),
    ]

    # Page 3 - Bootstrap
    story += [
        p("2. Bootstrap the GitHub Research Repository", "h1"),
        p("Once the Agent and Skills are available in ChatGPT, initialize the target repository around one bounded root research question.", "body"),
        p("Bootstrap prompt", "h2"),
        code_box("""Initialize OWNER/REPOSITORY as a Research-Agent project around the question:
\"<ROOT RESEARCH QUESTION>\"

Use the existing material in <PATH> as supplied background.
Do not invent research conclusions or future tasks."""),
        Spacer(1, 0.12 * inch),
        p("The bootstrap workflow inspects the repository first, preserves compatible existing material, and creates project-local authorities and research state. The root task starts pending; bootstrap organizes the research but does not solve it.", "body"),
        p("Typical project structure", "h2"),
        code_box("""README.md
AGENTS.md                  # local operating authority
dictionary.md              # terminology / notation
roadmap.yaml               # canonical structured roadmap
ROADMAP.md                 # human-readable projection
research-agent.lock.json   # toolchain pin when metadata is available
Tasks/                     # task contracts, evidence, resolutions
Background/                # genuinely shared foundations
templates/
history/
checks/"""),
        Spacer(1, 0.12 * inch),
        p("Three files that are easy to confuse", "h2"),
        Table([
            [p("File", "table_b"), p("Lives where?", "table_b"), p("Purpose", "table_b")],
            [p("RESEARCH_AGENT.md", "table"), p("Research-Agent distribution / agent config", "table"), p("How the collaborator behaves", "table")],
            [p("AGENTS.md", "table"), p("Your research repository", "table"), p("Local project rules and authority", "table")],
            [p("research-agent.lock.json", "table"), p("Your research repository", "table"), p("Which external toolchain version the project expects", "table")],
        ], colWidths=[1.55 * inch, 2.05 * inch, CONTENT_W - 3.60 * inch], repeatRows=1, style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ])),
        Spacer(1, 0.12 * inch),
        callout("Authority rule", "The project's current AGENTS.md governs project-local behavior. A reusable Skill supplies procedure and the lock supplies compatibility metadata; neither overrides project authority.", "teal"),
        PageBreak(),
    ]

    # Page 4 - Workflow
    story += [
        p("3. Use the Workflow Day to Day", "h1"),
        p("Ordinary research is conversational. Name the current task and the bounded question; the Agent reads the repository and stops at meaningful decision points instead of autonomously finishing the task.", "body"),
        p("Bounded research prompt", "h2"),
        code_box("""Work with me on T002. For this turn, determine whether the current
assumptions are sufficient for the proposed bound. Do not continue to
later proof steps."""),
        Spacer(1, 0.12 * inch),
        p("Standardized procedures", "h2"),
        Table([
            [p("Goal", "table_b"), p("Natural-language request", "table_b")],
            [p("Define", "table_b"), p("Define a new task under T002 for this obstruction.", "table")],
            [p("Review", "table_b"), p("Review the current lemma adversarially.", "table")],
            [p("Evidence", "table_b"), p("Transcribe the verified proof as evidence for T002.", "table")],
            [p("Restructure", "table_b"), p("Make this obstruction a sibling task and preserve history.", "table")],
            [p("Complete", "table_b"), p("Evaluate T002 for completion and complete it only if supported.", "table")],
            [p("Validate", "table_b"), p("Validate this branch against the current project rules.", "table")],
            [p("Synthesize", "table_b"), p("Synthesize the completed tasks into a paper-level outline.", "table")],
        ], colWidths=[1.18 * inch, CONTENT_W - 1.18 * inch], repeatRows=1, style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE_GRAY]),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])),
        Spacer(1, 0.12 * inch),
        callout("Research stays user-directed", "Defining a task does not authorize solving it. Saving evidence does not imply completion. Completion is a separate explicit workflow, and negative or inconclusive outcomes can be legitimate results when supported.", "blue"),
        p("Repository writes", "h2"),
        p("For substantive changes, expect a scoped branch, the smallest coherent mutation, validation, and a reviewable pull request unless your project explicitly authorizes another write path.", "body"),
        PageBreak(),
    ]

    # Page 5 - Upgrade + checklist
    story += [
        p("4. Upgrade Safely", "h1"),
        p("Do not make a research project follow Research-Agent/main automatically. Treat a newer release as a compatibility event that must be reviewed and intentionally accepted.", "body"),
        step_table([
            ("1", "Inspect", "Read the release changes and identify Agent/Skill contracts that changed."),
            ("2", "Install", "Update the relevant Agent instructions and Skill packages in ChatGPT."),
            ("3", "Test", "Exercise representative workflows against a project branch."),
            ("4", "Compare", "Compare the new distribution with research-agent.lock.json."),
            ("5", "Reconcile", "Make any project-local changes required by the new workflow."),
            ("6", "Accept", "Update the lock only after intentionally accepting the new release."),
        ]),
        Spacer(1, 0.15 * inch),
        p("Compatibility check", "h2"),
        code_box("""python scripts/check_project_compatibility.py \\
  /path/to/project/research-agent.lock.json \\
  --distribution /path/to/research-agent-distribution.json"""),
        Spacer(1, 0.14 * inch),
        callout("A mismatch is a review signal", "A version or commit mismatch does not authorize an automatic migration. The project lock records the external toolchain a project expects; project-local AGENTS.md and current research state remain authoritative.", "teal"),
        p("Quick-start checklist", "h2"),
        Table([
            [p("[ ]", "table_b"), p("GitHub research repository exists and ChatGPT can access it.", "table")],
            [p("[ ]", "table_b"), p("RESEARCH_AGENT.md is configured as persistent collaborator behavior.", "table")],
            [p("[ ]", "table_b"), p("Required Skills are installed independently from one version.", "table")],
            [p("[ ]", "table_b"), p("The repository has been bootstrapped around one root question.", "table")],
            [p("[ ]", "table_b"), p("Project-local AGENTS.md is treated as the operating authority.", "table")],
            [p("[ ]", "table_b"), p("The toolchain is pinned when concrete distribution metadata is available.", "table")],
            [p("[ ]", "table_b"), p("Research proceeds through bounded, user-directed task conversations.", "table")],
        ], colWidths=[0.42 * inch, CONTENT_W - 0.42 * inch], style=TableStyle([
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [WHITE, PALE_GRAY]),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])),
        Spacer(1, 0.16 * inch),
        p("Canonical source: AidanRDonahue/Research-Agent. For the full walkthrough, see USING_IN_YOUR_PROJECT.md in the repository.", "small"),
    ]

    doc.build(story)


def render_verify(pdf: Path, render_dir: Path):
    """Render all pages with PyMuPDF and perform basic page-image sanity checks."""
    import fitz

    render_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    if len(doc) != 5:
        raise SystemExit(f"expected 5 pages, found {len(doc)}")
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False)
        if pix.width < 900 or pix.height < 1100:
            raise SystemExit(f"rendered page {i+1} is unexpectedly small: {pix.width}x{pix.height}")
        pix.save(render_dir / f"page-{i+1}.png")
    print(f"verified {len(doc)} rendered pages in {render_dir}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist/research-agent-installation-guide.pdf")
    parser.add_argument("--render-dir", default="dist/rendered-installation-guide")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    build_pdf(output)
    render_verify(output, Path(args.render_dir))
    print(f"built {output}")


if __name__ == "__main__":
    main()
