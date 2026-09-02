"""
Life Science Chapter 1 (God's Living World) practice test - HARD version.
Source of truth for BOTH the PDF (build.py) and the online quiz (gen_js.py).

Ryan's rules:
  - every question is multiple choice, true/false, or answered from a word bank
  - answer key is always a separate PDF
  - no em dash, no en dash, no tilde anywhere

Difficulty targets (deliberately above the LCA Version 2 objective test):
  - scenario and application items, not definition lookup
  - distractors drawn from the SAME category so elimination does not work
  - multi step reasoning on classification ranks
  - true/false items that turn on a subtle distinction, not an obvious flip
  - word banks always carry extra terms that are close cousins of the answers
"""

TITLE = "Life Science"
SUBTITLE = "Chapter 1: God's Living World"
COURSE_LABEL = "LCA 7th Grade Life Science"
VERSION_LABEL = "Chapter 1 Practice Test"

# ---------------------------------------------------------------------------
# Part A: Vocabulary matching from a word bank with 4 extra terms.
# Definitions are reworded from the notes so this is not a lookup exercise.
# ---------------------------------------------------------------------------
MATCHING_TERMS = [
    "worldview", "naturalism", "ethics", "homeostasis",
    "hypothesis", "scientific inquiry", "variable", "control group",
    "data", "polyphenism", "cell", "scientific name",
    "model", "taxonomy", "theory", "law",          # last four are the extras
]
MATCHING_ITEMS = [
    ("the overarching narrative a person uses to interpret everything they see", "worldview"),
    ("the belief that living things arose through completely natural processes", "naturalism"),
    ("the study of applying moral principles to life", "ethics"),
    ("an organism's ability to hold its internal processes steady while its surroundings change", "homeostasis"),
    ("an explanation built on a limited number of observations", "hypothesis"),
    ("using a variety of tools and skills to answer a question or solve a problem", "scientific inquiry"),
    ("the one factor that is changed in a controlled experiment", "variable"),
    ("the group in an experiment that is not exposed to the independent variable", "control group"),
    ("information that people collect", "data"),
    ("the change of form the dead leaf butterfly uses for camouflage", "polyphenism"),
    ("the smallest working unit of an organism", "cell"),
    ("the unique two part name that identifies an organism", "scientific name"),
]

# ---------------------------------------------------------------------------
# Part B: Multiple choice.  (stem, options, index of correct answer)
# ---------------------------------------------------------------------------
MULTIPLE_CHOICE = [
    ("Maria sets up two identical terrariums with the same soil, water, and light. She mixes fertilizer into one and leaves the other alone, then measures how tall the plants grow. What is the variable in her experiment?",
     ["the amount of water each terrarium receives",
      "the fertilizer mixed into one terrarium",
      "the type of soil in both terrariums",
      "the height the plants reach"],
     1),
    ("In Maria's experiment above, which terrarium is the control group?",
     ["the terrarium with fertilizer",
      "the terrarium without fertilizer",
      "both terrariums, since they started the same",
      "neither one, because she measured both"],
     1),
    ("Which of these is written correctly as a hypothesis using the sentence frame from the notes?",
     ["Why do plants grow taller when they are fertilized?",
      "Fertilizer might possibly help plants in some way.",
      "If fertilizer is responsible for plant growth, then fertilized plants will grow taller.",
      "Fertilized plants are the prettiest plants in the room."],
     2),
    ("A classmate says his hypothesis is that studying creation pleases God. Why is that statement not a scientific hypothesis?",
     ["It is not written in a complete sentence.",
      "There is no experiment that could test it or show it to be wrong.",
      "It does not mention any living things.",
      "It is written with words instead of numbers."],
     1),
    ("Which list contains only quantitative data?",
     ["dark green leaves, waxy texture, 12 leaves",
      "14 centimeters tall, 12 leaves, 22 degrees Celsius",
      "sweet smell, 14 centimeters tall, wilted stem",
      "8 seeds, rough texture, bright red petals"],
     1),
    ("After years of collecting data, a scientist proposes an explanation for why organisms keep stable internal conditions. What has she proposed?",
     ["a law, because it describes what she observed",
      "a theory, because it explains the data she collected",
      "a hypothesis, because she has only limited observations",
      "a model, because it simplifies the real world"],
     1),
    ("Which statement about the levels of classification is correct?",
     ["A family contains more kinds of organisms than an order.",
      "A phylum contains more kinds of organisms than a class.",
      "A genus contains more kinds of organisms than a family.",
      "A species contains more kinds of organisms than a kingdom."],
     1),
    ("Two organisms belong to the same order but to different families. Which statement must also be true?",
     ["They belong to the same genus.",
      "They belong to the same class.",
      "They belong to the same species.",
      "They belong to different domains."],
     1),
    ("The scientific name of the red maple is Acer rubrum. What does Acer tell you?",
     ["its species", "its genus", "its family", "its domain"],
     1),
    ("Two organisms both make their own food using energy from their environment. One has a nucleus and the other does not. How are they best described?",
     ["Both are heterotrophs, and one is eukaryotic while the other is prokaryotic.",
      "Both are autotrophs, and one is eukaryotic while the other is prokaryotic.",
      "Both are autotrophs, and both are eukaryotic.",
      "Both are prokaryotic, and one is an autotroph while the other is a heterotroph."],
     1),
    ("A mushroom absorbs nutrients from a rotting log. Based on the notes, a mushroom is",
     ["an autotroph, because it does not move from place to place",
      "a heterotroph, because it gets its energy from other organisms",
      "a prokaryote, because its cells have no nucleus",
      "unicellular, because it grows in one spot"],
     1),
    ("A student writes that Christians and naturalists both believe reality is real and can be observed. According to the chart in the notes, this statement is",
     ["correct, because the notes list the same answer for both groups on those points",
      "incorrect, because naturalists believe reality cannot be observed",
      "incorrect, because Christians believe observations are not intelligible",
      "incorrect, because only naturalists study reality"],
     0),
    ("Both Christians and naturalists say man is responsible for the earth. According to the notes, how do their reasons differ?",
     ["The Christian says it is God's command, and the naturalist says we need the earth to last.",
      "The Christian says we need the earth to last, and the naturalist says it is God's command.",
      "Both groups give exactly the same reason.",
      "Neither group gives a reason for the responsibility."],
     0),
    ("Which characteristic of life does the phrase \"sometimes developing into quite different forms\" describe?",
     ["organization via cells",
      "intakes energy",
      "demonstrates development",
      "reproduction by kind to kind"],
     2),
    ("According to the notes, what problem comes from altering the classification system to show evolutionary relationships?",
     ["Scientific names would become too long to use.",
      "It violates God's law of nature that organisms reproduce after their kind.",
      "Taxonomy could no longer sort organisms into groups.",
      "Christians would no longer be able to use classification at all."],
     1),
    ("Which statement best describes how classification relates to worldview in the notes?",
     ["Classification can only support an evolutionary view of life.",
      "Classification can only support a biblical view of life.",
      "Classification can support a biblical view of life, though naturalists use the taxonomic tree for evolutionary support.",
      "Classification is the one part of science that no worldview affects."],
     2),
    ("Which of these is NOT one of the characteristics of life listed in the notes?",
     ["response to stimuli in the environment",
      "organization via cells",
      "movement from place to place",
      "reproduction by kind to kind"],
     2),
    ("In the scientific method as listed in the notes, which step comes immediately after testing?",
     ["observe", "communicate", "analyze and draw conclusions", "form a hypothesis"],
     2),
]

# ---------------------------------------------------------------------------
# Part C: One blank per sentence, filled from a 22 term word bank (8 extras).
# ---------------------------------------------------------------------------
FILL_WORD_BANK = [
    "prokaryotic", "heterotroph", "nucleus", "qualitative", "quantitative",
    "control", "theory", "law", "genus", "intelligent",
    "Creation Mandate", "model", "multicellular", "taxonomy",
    "eukaryotic", "autotroph", "hypothesis", "experimental",
    "variable", "species", "homeostasis", "unicellular",
]
FILL_IN = [
    ("A cell that has no nucleus is called a(n) {} cell.", ["prokaryotic"]),
    ("An organism that must eat other organisms to get its energy is a(n) {}.", ["heterotroph"]),
    ("The structure that holds and protects the DNA in a eukaryotic cell is the {}.", ["nucleus"]),
    ("A record that reads \"dark green and waxy\" is {} data.", ["qualitative"]),
    ("A record that reads \"14 centimeters tall\" is {} data.", ["quantitative"]),
    ("In a controlled experiment, the group that is not exposed to the independent variable is the {} group.", ["control"]),
    ("An idea that scientists use to explain the data they have collected is a(n) {}.", ["theory"]),
    ("An idea that scientists use to describe what they observe is a(n) {}.", ["law"]),
    ("The seventh level of classification, and the first word of a scientific name, is the {}.", ["genus"]),
    ("Disorder naturally increases, so order only increases with {} effort.", ["intelligent"]),
    ("God's command to Adam and Eve to fill the earth and have dominion over it is the {}.", ["Creation Mandate"]),
    ("A simplified explanation, description, or representation of the world is a(n) {}.", ["model"]),
    ("An organism built from more than one cell is {}.", ["multicellular"]),
    ("The science of sorting organisms into groups is {}.", ["taxonomy"]),
]

# ---------------------------------------------------------------------------
# Part D: True or false.  Each turns on a distinction, not an obvious flip.
# (statement, is_true, why)
# ---------------------------------------------------------------------------
TRUE_FALSE = [
    ("A hypothesis must be refutable, which means it must be possible to show that it is wrong.",
     True, "Refutable is one of the five marks of a good hypothesis."),
    ("A hypothesis that cannot be tested is still scientific as long as it is descriptive.",
     False, "A good hypothesis is descriptive, predictable, refutable, testable, and repeatable. Testable is required."),
    ("The control group and the experimental group are treated the same in every way except the independent variable.",
     True, "That is what makes a controlled experiment examine one factor at a time."),
    ("A scientific law explains why something happens, and a theory describes what scientists observe.",
     False, "It is the other way around. A law describes what scientists observe; a theory explains the data they collected."),
    ("According to the notes, Christians and naturalists both hold that reality can be observed.",
     True, "The chart lists the same answer for both groups: reality is real, it can be observed, and observations are intelligible."),
    ("According to the notes, only Christians say man is responsible for the earth.",
     False, "Both say man is responsible. Christians say it is God's command; naturalists say we need the earth to last."),
    ("Every eukaryotic organism is multicellular.",
     False, "Eukaryotic means the cell has a nucleus. That says nothing about how many cells the organism has."),
    ("Every autotroph is a prokaryote.",
     False, "Autotroph describes how an organism gets energy. Prokaryote describes whether its cells have a nucleus."),
    ("Two organisms in the same family must also be in the same order.",
     True, "Order is a broader level than family, so anything sharing a family also shares every level above it."),
    ("Two organisms in the same class must also be in the same genus.",
     False, "Genus is far more specific than class. Sharing a class says nothing about sharing a genus."),
    ("Homeostasis means an organism's internal conditions never change at all.",
     False, "Homeostasis is the ability to keep internal processes stable by reacting to internal and external stimuli."),
    ("The notes say God values animal life, and values human life more.",
     True, "Luke 12:22 through 34 is cited for both points."),
]

# ---------------------------------------------------------------------------
# Part E: Worldview chart, answered from a word bank.
# ---------------------------------------------------------------------------
CHART_EXAMPLE = ("responsibility for earth", "man (God's command)", "man (need the earth to last)")
CHART_ROWS = [
    ("ultimate source of truth", "God's Word", "naturalistic science"),
    ("source of life", "God", "natural means"),
    ("persistence of pain", "result of the Fall", "inevitable"),
    ("extent of death", "eternal life in heaven or hell", "end of existence"),
]
CHART_WORD_BANK = ["natural means", "God's Word", "end of existence", "result of the Fall",
                   "naturalistic science", "eternal life in heaven or hell", "God", "inevitable"]

# ---------------------------------------------------------------------------
# Part F: Levels of classification, ordered from a word bank.
# ---------------------------------------------------------------------------
CLASSIFICATION_LEVELS = ["domain", "kingdom", "phylum", "class", "order", "family", "genus", "species"]
LEVEL_WORD_BANK = ["family", "domain", "species", "class", "kingdom", "genus", "phylum", "order"]
CLASSIFICATION_MNEMONIC = "Dear King Philip Came Over For Good Soup"

# ---------------------------------------------------------------------------
# Part G: three points each, still no writing.
#   multi: circle all that apply     order: number the steps     mc: best answer
# ---------------------------------------------------------------------------
SHORT_ANSWER = [
    {"type": "multi",
     "q": "Which of these are the five characteristics of life? Circle all five.",
     "n": 5,
     "options": [("intakes energy", True), ("moves from place to place", False),
                 ("organization via cells", True), ("contains a nucleus", False),
                 ("reproduction by kind to kind", True), ("can be seen without a microscope", False),
                 ("demonstrates development", True), ("is made mostly of water", False),
                 ("response to stimuli in the environment", True), ("has a brain", False)]},
    {"type": "order",
     "q": "Number the steps of the scientific method in order, 1 to 4.",
     "steps": ["observe", "test", "analyze and draw conclusions", "communicate"],
     "shown": ["communicate", "test", "observe", "analyze and draw conclusions"]},
    {"type": "multi",
     "q": "Which of these are the five marks of God's purposeful design in living things? Circle all five.",
     "n": 5,
     "options": [("growth", True), ("movement", False), ("organization", True), ("color", False),
                 ("reproduction", True), ("energy", True), ("size", False), ("response", True),
                 ("speed", False), ("symmetry", False)]},
    {"type": "multi",
     "q": "Which of these make humans a distinct creation, different from other living things? Circle all six.",
     "n": 6,
     "options": [("made in the image of God", True), ("have more cells than any other organism", False),
                 ("have higher value", True), ("are the fastest creatures on earth", False),
                 ("have responsibilities", True), ("punished for killing man", True),
                 ("do not need to intake energy", False), ("have moral agency", True),
                 ("are the only organisms that reproduce", False), ("have a plan for salvation", True)]},
    {"type": "multi",
     "q": "Which of these describe a good hypothesis? Circle all five.",
     "n": 5,
     "options": [("descriptive", True), ("proven true before it is tested", False), ("predictable", True),
                 ("written using only numbers", False), ("refutable", True), ("impossible to show wrong", False),
                 ("testable", True), ("always about living things", False), ("repeatable", True),
                 ("kept secret until the end", False)]},
    {"type": "multi",
     "q": "On which points do Christians and naturalists AGREE, according to the chart in the notes? Circle all four.",
     "n": 4,
     "options": [("reality is real", True), ("the ultimate source of truth", False),
                 ("reality can be observed", True), ("the source of life", False),
                 ("observations are intelligible", True), ("the persistence of pain", False),
                 ("man is responsible for the earth", True), ("the extent of death", False)]},
]

# Notes for Ryan, printed at the end of the answer key only.
NOTES_FOR_PARENT = [
    "This version is built to run harder than the LCA Version 2 objective test. The distractors in Part B are pulled "
    "from the same category as the answer, so Max cannot cross off the odd one out and guess.",
    "The items most likely to trip him up, and the ones worth reviewing together: B7 and B8 and D9 and D10 "
    "(reasoning up and down the classification ranks), B12 and D5 and G6 (the places where Christians and naturalists "
    "actually AGREE in the chart), and D7 and D8 (nucleus versus number of cells, and how an organism gets energy).",
    "Levels of classification: the seventh level is <b>genus</b> (Max wrote \"Genius\" on his notes). "
    "Genus plus species makes the scientific name.",
    "The nucleus \"holds and protects the <b>DNA</b>\" in a eukaryotic cell. That blank on his notes is hard to read.",
    "In section 1.1 the term for \"God's command to Adam and Eve to fill the earth and have dominion over it\" is the "
    "<b>Creation Mandate</b>, not just \"creation.\"",
]


# ===========================================================================
# ONLINE ONLY.  The web quiz runs harder than the paper test in four ways:
#   1. this extra challenge round, which is not on the PDF
#   2. bigger word banks (the decoys below are added to the online banks only)
#   3. "select all that apply" without telling him how many are correct
#   4. answer choices are reshuffled on every attempt, so retaking it cannot
#      be passed by memorizing letter positions
# ===========================================================================
ONLINE_MATCH_DECOYS = ["organism", "autotroph", "genus", "stimulus"]
ONLINE_FILL_DECOYS = ["qualitative data", "scientific inquiry", "domain", "camouflage",
                      "redemption", "development"]

ONLINE_EXTRA_MC = [
    ("Two organisms share a phylum but belong to different classes. Which statement must be true?",
     ["They share a kingdom.",
      "They share an order.",
      "They share a family.",
      "They belong to different domains."],
     0),
    ("An oak is named Quercus alba and another tree is named Quercus rubra. What must be true of the two trees?",
     ["They are the same species but different genera.",
      "They are in the same genus but are different species.",
      "They are in the same species but different families.",
      "They are in different kingdoms."],
     1),
    ("Caleb wants to find out whether fertilizer helps plants grow. He gives the fertilized plant more sunlight than the other one. What is wrong with his experiment?",
     ["He should have used qualitative data instead of quantitative data.",
      "He changed more than one factor, so he cannot tell which one caused the difference.",
      "He needed a hypothesis written as a question.",
      "He should have measured the plants only once."],
     1),
    ("A dog pants on a hot afternoon. Which statement best explains what is happening?",
     ["It is reproducing after its kind.",
      "It is maintaining homeostasis by reacting to an external stimulus.",
      "It is demonstrating development into a different form.",
      "It is showing that order increases without intelligent effort."],
     1),
    ("Which statement would BOTH a Christian and a naturalist in the notes affirm?",
     ["The ultimate source of truth is God's Word.",
      "Death is the end of existence.",
      "Observations of reality are intelligible.",
      "Pain is a result of the Fall."],
     2),
    ("Which of these hypotheses is refutable?",
     ["Invisible forces that leave no trace cause plants to grow.",
      "Plants given fertilizer will grow taller than plants given none.",
      "Plants are the most beautiful part of creation.",
      "Something unknown affects plants in some unknown way."],
     1),
    ("A student says a theory turns into a law once scientists have tested it enough times. Why is that wrong?",
     ["Laws come first, and theories are built from them later.",
      "A law describes what is observed and a theory explains collected data, so one does not become the other.",
      "Only hypotheses can become laws.",
      "Theories and laws both describe observations, so nothing changes."],
     1),
    ("A single celled organism makes its own food using energy from its environment, and its cell has no nucleus. Which set of terms describes it?",
     ["multicellular, heterotroph, eukaryotic",
      "unicellular, autotroph, prokaryotic",
      "unicellular, heterotroph, prokaryotic",
      "multicellular, autotroph, eukaryotic"],
     1),
]

ONLINE_EXTRA_TF = [
    ("An organism can be both an autotroph and a prokaryote at the same time.",
     True, "Those two words answer different questions: how it gets energy, and whether its cells have a nucleus."),
    ("Because a theory explains data, a theory is a weaker guess than a hypothesis.",
     False, "A hypothesis rests on limited observations. A theory explains data that scientists have collected."),
    ("Two organisms in the same genus are automatically in the same family.",
     True, "Family is broader than genus, so anything sharing a genus shares every level above it."),
    ("According to the notes, a naturalist and a Christian would give the same answer for the extent of death.",
     False, "The naturalist says death is the end of existence. The Christian says eternal life in heaven or hell."),
]
