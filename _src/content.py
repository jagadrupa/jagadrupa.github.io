"""All site content lives here. build.py checks every note reference against the PDF."""

REPO_CN = "https://github.com/jagadrupa/Computational_neuroscience"
REPO_NI = "https://github.com/jagadrupa/neuroimaging"
REPO_AD = "https://github.com/jagadrupa/Spatial_Alzheimers_AI_project"

SCALES = [
    ("molecules", "Molecules", "Channels, gates, transmitters, receptors",
     "How charged ions and signalling molecules create the raw material of neural signals."),
    ("neurons", "Neurons", "Membranes, spikes, codes",
     "How one cell integrates its input, fires, and carries information."),
    ("networks", "Networks", "Synapses, circuits, learning rules",
     "What groups of connected neurons compute, and how their connections change."),
    ("brain", "Brain", "Anatomy, systems, imaging",
     "How regions are organised, supplied with blood, and measured in living people."),
    ("cognition", "Cognition", "Decisions, memory, language, reward",
     "How neural computation connects to choice, memory, language and behaviour."),
    ("disease", "Disease", "Alzheimer's and clinical signatures",
     "What changes in the diseased brain, and how carefully that change can be measured."),
]

DOCS = {
    "w1": ("uw-w1", "UW week 1"), "w2": ("uw-w2", "UW week 2"), "w3": ("uw-w3", "UW week 3"),
    "w4": ("uw-w4", "UW week 4"), "w5": ("uw-w5", "UW week 5"), "w6": ("uw-w6", "UW week 6"),
    "w7": ("uw-w7", "UW week 7"), "w8": ("uw-w8", "UW week 8"), "ni": ("jhu-neuro", "JHU notes"),
}

CERTS = {
    "uw": ("Computational Neuroscience", "University of Washington", "4 Sep 2026", "2026-09-04",
           "certificates/uw-computational-neuroscience", "https://coursera.org/verify/QVE1DFIYMOJN"),
    "jhu": ("Fundamental Neuroscience for Neuroimaging", "Johns Hopkins University", "13 Jul 2020", "2020-07-13",
            "certificates/jhu-neuroimaging", "https://coursera.org/verify/RN9MRJCZ256U"),
    "uchicago": ("Understanding the Brain: The Neurobiology of Everyday Life", "The University of Chicago", "13 Jul 2020", "2020-07-13",
                 "certificates/uchicago-brain", "https://coursera.org/verify/6UDPHE85PSS3"),
    "yale": ("Introduction to Psychology", "Yale University", "19 Jul 2020", "2020-07-19",
             "certificates/yale-psychology", "https://coursera.org/verify/DR5BAPD97DNZ"),
}

# Outcome: (scale, unit, statement, [note refs as (doc, section-title fragment)])
UW = [
 ("brain", "Week 1 · Basic neurobiology", "Separate descriptive, mechanistic and interpretive models of the same phenomenon, using receptive fields as the worked case.", [("w1", "The Three Models, Side by Side")]),
 ("neurons", "Week 1 · Basic neurobiology", "Explain how V1 receptive fields can be built from LGN input in the Hubel and Wiesel model.", [("w1", "Mechanistic Model")]),
 ("brain", "Week 1 · Basic neurobiology", "State the efficient coding hypothesis and how it accounts for the shape of receptive fields.", [("w1", "Interpretive Model")]),
 ("molecules", "Week 1 · Basic neurobiology", "Describe ionic channels as gatekeepers of the membrane potential.", [("w1", "Ionic Channels")]),
 ("neurons", "Week 1 · Basic neurobiology", "Trace the action potential, its propagation along the axon, and the role of myelin.", [("w1", "The Action Potential")]),
 ("networks", "Week 1 · Basic neurobiology", "Explain the synapse doctrine, Hebbian learning and spike-timing dependent plasticity.", [("w1", "The Synapse Doctrine"), ("w1", "Spike-Timing Dependent Plasticity")]),
 ("brain", "Week 1 · Basic neurobiology", "Tour the peripheral and central nervous systems and the cortex as a layered sheet.", [("w1", "Organization of the Nervous System"), ("w1", "The Cerebral Cortex")]),

 ("brain", "Week 2 · Neural encoding", "Compare recording methods from fMRI to patch clamp and what analysis each one permits.", [("w2", "Recording from the Brain")]),
 ("neurons", "Week 2 · Neural encoding", "Read raster plots and tuning curves, and say where the tuning-curve picture stops working.", [("w2", "Tuning Curves"), ("w2", "A Hierarchy of Complexity")]),
 ("networks", "Week 2 · Neural encoding", "Model centre-surround receptive fields as spatial filters using a difference of Gaussians.", [("w2", "Spatial Filtering")]),
 ("neurons", "Week 2 · Neural encoding", "Build the linear-nonlinear response model and explain why a linear filter alone is not enough.", [("w2", "Why a Linear Filter Cannot Be the Whole Story"), ("w2", "The Linear--Nonlinear Model")]),
 ("neurons", "Week 2 · Neural encoding", "Recover a neuron's feature from data with the spike-triggered average, and explain why white noise is the right stimulus.", [("w2", "Why White Noise?"), ("w2", "The Spike-Triggered Average")]),
 ("neurons", "Week 2 · Neural encoding", "Extend to several features with PCA and maximally informative dimensions.", [("w2", "Multiple Features"), ("w2", "Maximally Informative Dimensions")]),
 ("neurons", "Week 2 · Neural encoding", "Derive the Poisson model from coin flips, test it against data, and move to generalized linear models.", [("w2", "From Coin Flips"), ("w2", "Testing It Against Real Data"), ("w2", "Generalized Linear Models")]),

 ("cognition", "Week 3 · Neural decoding", "Apply signal detection theory and the likelihood ratio to a two-alternative decision.", [("w3", "Signal Detection Theory"), ("w3", "The Likelihood Ratio")]),
 ("cognition", "Week 3 · Neural decoding", "Explain how accumulating evidence over time trades speed against accuracy.", [("w3", "Accumulating Evidence Over Time")]),
 ("cognition", "Week 3 · Neural decoding", "Build priors and unequal error costs into a decision rule.", [("w3", "Priors: Building In"), ("w3", "Costs: Not All Mistakes")]),
 ("networks", "Week 3 · Neural decoding", "Decode direction with population vectors in cricket cercal cells and motor cortex, and say why that is not enough.", [("w3", "The Cricket Cercal System"), ("w3", "The Same Trick in Motor Cortex"), ("w3", "Why the Population Vector Is Not Enough")]),
 ("networks", "Week 3 · Neural decoding", "Work through Bayesian decoding with maximum likelihood and maximum a posteriori estimates.", [("w3", "Bayesian Inference"), ("w3", "Maximum Likelihood"), ("w3", "Maximum a Posteriori")]),
 ("brain", "Week 3 · Neural decoding", "Describe stimulus reconstruction from LGN spike trains and from human fMRI.", [("w3", "Reading Minds I"), ("w3", "Reading Minds II")]),
 ("neurons", "Week 3 · Neural decoding", "Explain where the retina must place its threshold to detect single photons, and the role of the prior.", [("w3", "Where the Threshold Has to Live"), ("w3", "The Resolution: the Prior")]),

 ("neurons", "Week 4 · Information theory", "Define entropy, noise entropy and mutual information, including their limiting cases.", [("w4", "Entropy: Average Information"), ("w4", "Noise Entropy"), ("w4", "Mutual Information")]),
 ("neurons", "Week 4 · Information theory", "Estimate information from spike patterns and recognise undersampling bias.", [("w4", "Method 1"), ("w4", "Sampling and Bias")]),
 ("neurons", "Week 4 · Information theory", "Compute information per single spike and apply it to place fields.", [("w4", "Method 2"), ("w4", "Place Fields")]),
 ("brain", "Week 4 · Information theory", "Explain efficient coding of natural stimuli: Laughlin's test, real-time adaptation, redundancy reduction and sparse coding.", [("w4", "Laughlin"), ("w4", "Adapting in Real Time"), ("w4", "Redundancy Reduction"), ("w4", "Sparse Coding")]),

 ("molecules", "Week 5 · Computing in carbon", "Treat ionic gradients as batteries and ion channels as stochastic pores, each ion with its own equilibrium potential.", [("w5", "The Cell Has a Battery"), ("w5", "Ion Channels"), ("w5", "Each Ion Has Its Own Battery")]),
 ("molecules", "Week 5 · Computing in carbon", "Write gate kinetics for potassium activation and sodium activation with inactivation.", [("w5", "Inside the Potassium Channel"), ("w5", "The Kinetics of One Gate"), ("w5", "Sodium: Activation and Inactivation")]),
 ("neurons", "Week 5 · Computing in carbon", "Derive the passive membrane equation from an RC circuit.", [("w5", "The Membrane as an RC Circuit"), ("w5", "The Passive Membrane Equation")]),
 ("neurons", "Week 5 · Computing in carbon", "Assemble the Hodgkin-Huxley equations and read a spike as a separation of timescales.", [("w5", "The Hodgkin--Huxley Equations"), ("w5", "Anatomy of a Spike")]),
 ("neurons", "Week 5 · Computing in carbon", "Reduce the neuron to integrate-and-fire, theta and two-variable models, and analyse them in the phase plane.", [("w5", "Integrate-and-Fire"), ("w5", "The Theta Neuron"), ("w5", "The Phase Plane")]),
 ("neurons", "Week 5 · Computing in carbon", "Use the cable equation and compartmental models to reason about dendritic computation.", [("w5", "The Cable Equation"), ("w5", "Compartmental Models"), ("w5", "What Dendrites Add")]),

 ("molecules", "Week 6 · Computing with networks", "Model synaptic conductance from release probability and channel-opening kinetics.", [("w6", "What Sets the Synaptic Conductance")]),
 ("neurons", "Week 6 · Computing with networks", "Add a synapse to the membrane equation as one more conductance branch.", [("w6", "Putting a Synapse In")]),
 ("networks", "Week 6 · Computing with networks", "Move from spiking networks to firing-rate models and say what each gives up.", [("w6", "Spiking or Firing Rate?"), ("w6", "The Firing-Rate Model")]),
 ("networks", "Week 6 · Computing with networks", "Analyse linear recurrent networks with eigenvectors: stability and selective amplification.", [("w6", "Eigenvectors to the Rescue"), ("w6", "Eigenvalues Determine Stability"), ("w6", "Amplification")]),
 ("networks", "Week 6 · Computing with networks", "Explain nonlinear recurrent behaviour and analyse excitatory-inhibitory circuits with linear stability analysis.", [("w6", "Nonlinear Recurrent Networks"), ("w6", "Non-Symmetric Networks"), ("w6", "Linear Stability Analysis")]),

 ("networks", "Week 7 · Networks that learn", "Formalise LTP, LTD and Hebb's rule, then show why plain and covariance rules are unstable.", [("w7", "Two Experimental Facts"), ("w7", "The Covariance Rule"), ("w7", "Are These Rules Stable?")]),
 ("networks", "Week 7 · Networks that learn", "Show how Oja's rule stabilises learning and what Hebbian learning computes, including where PCA fails.", [("w7", "Oja's Rule"), ("w7", "What Does Hebbian Learning Actually Do?"), ("w7", "Where PCA Fails")]),
 ("networks", "Week 7 · Networks that learn", "Connect competitive learning, self-organising maps and the EM algorithm for mixtures of Gaussians.", [("w7", "The Competitive Learning Algorithm"), ("w7", "Self-Organising Maps"), ("w7", "The EM Algorithm")]),
 ("brain", "Week 7 · Networks that learn", "Derive sparse coding from a generative model and describe predictive coding.", [("w7", "The Generative Model: A Sparse Prior"), ("w7", "What the Network Learns"), ("w7", "Predictive Coding")]),

 ("networks", "Week 8 · Supervision and reward", "Describe the perceptron and its learning rule, and why it cannot learn XOR.", [("w8", "The Perceptron Learning Rule"), ("w8", "What Perceptrons Cannot Do")]),
 ("networks", "Week 8 · Supervision and reward", "Train multilayer networks with sigmoid units by backpropagation.", [("w8", "Continuous Outputs"), ("w8", "Learning Multilayer Networks")]),
 ("cognition", "Week 8 · Supervision and reward", "Derive temporal difference learning and relate its prediction error to dopamine neurons.", [("w8", "Temporal Difference Learning"), ("w8", "Dopamine")]),
 ("cognition", "Week 8 · Supervision and reward", "Use actor-critic learning to go from prediction to action, and relate it to the basal ganglia.", [("w8", "Values Solve the Action Problem"), ("w8", "Actor--Critic Learning"), ("w8", "The Basal Ganglia")]),
]

NI = [
 ("neurons", "Structure and development", "Identify the parts of a neuron and the roles of glia, including myelin.", [("ni", "The Parts of a Neuron"), ("ni", "Glia")]),
 ("brain", "Structure and development", "Compare four ways of dividing the brain, from cytoarchitecture to connectivity-defined networks.", [("ni", "Four Ways of Dividing the Brain")]),
 ("brain", "Structure and development", "Explain how the brain develops and which features are conserved across species.", [("ni", "The Same Brain, Different Sizes"), ("ni", "How the Brain Is Built")]),
 ("brain", "Structure and development", "Trace arterial supply to the brain and its cortical vascular territories.", [("ni", "The Route In"), ("ni", "Vascular Territories")]),
 ("brain", "Structure and development", "Use anatomical axes, planes and relative-position terms, and avoid the left-right imaging trap.", [("ni", "Axes: Animals and Humans"), ("ni", "Planes"), ("ni", "Left Versus Right")]),

 ("molecules", "Signalling", "Explain the resting potential and synaptic transmission step by step.", [("ni", "The Resting Potential"), ("ni", "Synaptic Transmission, Step by Step")]),
 ("neurons", "Signalling", "Explain excitation, inhibition and summation, and what different electrodes record.", [("ni", "Excitation, Inhibition and Summation"), ("ni", "What an Electrode Records")]),
 ("molecules", "Signalling", "Describe AMPA and NMDA receptors and how drugs interfere with transmission.", [("ni", "Glutamate, AMPA and NMDA"), ("ni", "How Drugs Interfere")]),
 ("molecules", "Signalling", "Describe the blood-brain barrier as both protection and delivery problem.", [("ni", "The Blood--Brain Barrier")]),
 ("disease", "Signalling", "Link acetylcholine, dopamine and glutamate to their clinical signatures in Alzheimer's, Parkinson's, schizophrenia and ALS.", [("ni", "Four Transmitters and Their Clinical Signatures")]),

 ("brain", "Functional anatomy", "Map motor and somatosensory cortex, thalamic relay and contralateral crossing.", [("ni", "The Two Homunculi"), ("ni", "The Thalamus, and Crossing Over")]),
 ("brain", "Functional anatomy", "Describe visual cortex organisation and the cerebellum's settled and open roles.", [("ni", "Visual Cortex"), ("ni", "Cerebellum")]),

 ("cognition", "Cognition and assessment", "Use lesion cases to reason about language: the Broca and Wernicke dissociation.", [("ni", "Language: Broca and Wernicke")]),
 ("cognition", "Cognition and assessment", "Use the cases of Phineas Gage, H.M. and E.P. to reason about personality and memory.", [("ni", "Personality: Phineas Gage"), ("ni", "Memory: H.M. and E.P."), ("ni", "The Mirror-Drawing Result")]),
 ("cognition", "Cognition and assessment", "Explain the cognition-performance distinction and how scores are compared.", [("ni", "The Cognition--Performance Distinction"), ("ni", "What a Score Is Compared Against")]),
 ("cognition", "Cognition and assessment", "Describe memory and executive function tests such as the Wechsler Memory Scale, Stroop and Tower of London.", [("ni", "Memory Tests"), ("ni", "Executive Function Tests")]),

 ("brain", "Imaging methods", "Compare EEG, CT, SPECT, PET and MRI by what they measure and how well they localise.", [("ni", "EEG"), ("ni", "SPECT and PET"), ("ni", "MRI")]),
 ("disease", "Imaging methods", "Describe PET tracers used for glucose metabolism, amyloid and tau.", [("ni", "SPECT and PET")]),
 ("brain", "Imaging methods", "Explain MRI physics: relaxation, and how gradients give a measurement its location.", [("ni", "Two Relaxations"), ("ni", "Giving the Measurement a Location")]),
 ("brain", "Imaging methods", "Explain the BOLD signal and the haemodynamic response function, and what BOLD correlates with.", [("ni", "Oxygenated and Deoxygenated Blood"), ("ni", "The Haemodynamic Response Function"), ("ni", "What Is BOLD Correlated With?")]),
 ("brain", "Imaging methods", "Choose between volumetry, cortical thickness and voxel-based morphometry, and state their limits.", [("ni", "Volumetric Analysis"), ("ni", "Cortical Thickness"), ("ni", "Voxel-Based Morphometry"), ("ni", "Limitations")]),

 ("brain", "Experimental design", "Design block and event-related fMRI experiments and critique cognitive subtraction.", [("ni", "The Block Design"), ("ni", "The Event-Related Design"), ("ni", "Cognitive Subtraction"), ("ni", "Choosing a Control Condition")]),
 ("brain", "Experimental design", "Plan around scanner constraints and compare statistical designs.", [("ni", "Technical Limitations"), ("ni", "Five Statistical Designs")]),
 ("brain", "Experimental design", "Explain functional connectivity and the default mode network.", [("ni", "Correlation Instead of Contrast"), ("ni", "The Default Mode Network")]),
]

UCHI = "https://www.coursera.org/learn/neurobiology"
UCHICAGO = [
 ("brain", "Official course modules", "The nervous system"), ("neurons", "Official course modules", "Neural communication and embodied emotion"),
 ("brain", "Official course modules", "Neuroanatomy"), ("brain", "Official course modules", "Perception and vision"),
 ("brain", "Official course modules", "Hearing"), ("brain", "Official course modules", "The vestibular sense and gaze"),
 ("brain", "Official course modules", "Voluntary movements"), ("brain", "Official course modules", "Motor modulation"),
 ("brain", "Official course modules", "Homeostasis"), ("cognition", "Official course modules", "Abstract function"),
]
YALE_URL = "https://www.coursera.org/learn/introduction-psychology"
YALE = [
 ("cognition", "Official course modules", "Foundations: neuroscience, Freud, Skinner"),
 ("cognition", "Official course modules", "Development and language"),
 ("cognition", "Official course modules", "Cognition: perception, attention, memory"),
 ("cognition", "Official course modules", "Self and others: emotion, social psychology"),
 ("cognition", "Official course modules", "Variation: personality, intelligence, mental illness, therapy"),
 ("cognition", "Official course modules", "The good life: happiness"),
]
H1 = "https://www.edx.org/learn/neuroscience/harvard-university-fundamentals-of-neuroscience-part-1-the-electrical-properties-of-the-neuron"
H2 = "https://www.edx.org/learn/neuroscience/harvard-university-fundamentals-of-neuroscience-part-2-neurons-and-networks"
H3 = "https://www.edx.org/learn/neuroscience/harvard-university-fundamentals-of-neuroscience-part-3-the-brain"
HARV1 = [("molecules", "Official learning outcomes", "Fundamentals of bioelectricity"),
         ("neurons", "Official learning outcomes", "The importance of resting potential"),
         ("neurons", "Official learning outcomes", "The properties of passive membranes"),
         ("neurons", "Official learning outcomes", "Action potentials, their currents, and their role in the nervous system")]
HARV2 = [("molecules", "Official learning outcomes", "Basics of synapses"),
         ("networks", "Official learning outcomes", "How neurons communicate with each other"),
         ("networks", "Official learning outcomes", "How interconnected neurons in neuronal circuits interact with each other"),
         ("molecules", "Official learning outcomes", "The role of neuromodulation in the firing of synapses")]
HARV3 = [("brain", "Official learning outcomes", "How sensory perception works in the brain"),
         ("brain", "Official learning outcomes", "The physiology of vision, hearing, taste, smell, touch and motor control"),
         ("brain", "Official learning outcomes", "The basic anatomy of functional areas of the brain"),
         ("brain", "Official learning outcomes", "The visual system of the brain"),
         ("brain", "Official learning outcomes", "How the motor subsystems of the brain execute and coordinate movement"),
         ("brain", "Official learning outcomes", "The critical brain systems that keep us alive")]

AD_FINDINGS = [
 ("disease", "Original research", "The oligodendrocyte lineage is the main axis of disruption in this tissue, rising from 19.7% to 36.0% of cells.", "#biological-conclusions"),
 ("disease", "Original research", "Pathology is spatially zoned: AD-hot zones are about 58% oligodendrocyte, Preserved zones about 15%.", "#milestone-9--spatial-ad-zoning"),
 ("disease", "Original research", "The myelin programme fragments rather than simply declining; different myelin genes move in opposite directions.", "#the-myelin-module-fragments--the-central-oligodendrocyte-result"),
 ("disease", "Original research", "Core oligodendrocyte claims replicate in SEA-AD, an independent cohort (MAG, FDR 0.019).", "#external-validation-against-sea-ad"),
 ("disease", "Original research", "Limits stated up front: one section per condition, and a detection gap (median 28 vs 69 genes per cell) that confounds cross-section differential expression.", "#limitations"),
]

# id, title, provider, status, url, summary
COURSES = [
 dict(id="uw-computational-neuroscience", title="Computational Neuroscience", provider="University of Washington · Coursera", tutors="Rajesh P. N. Rao, Adrienne Fairhall", status="cert", cert="uw", url="https://www.coursera.org/learn/computational-neuroscience", outcomes=UW, kind="notes",
      summary="Eight weeks from encoding and decoding to learning and reward, written up as my own LaTeX notes.", repo=REPO_CN,
      graphic="uw", demos=["sta", "sdt", "entropy", "hh", "lif", "eigen", "oja", "perceptron", "td"]),
 dict(id="jhu-neuroimaging", title="Fundamental Neuroscience for Neuroimaging", provider="Johns Hopkins University · Coursera", tutors="Arnold Bakker", status="cert", cert="jhu", url="https://www.coursera.org/learn/neuroscience-neuroimaging", outcomes=NI, kind="notes",
      summary="Neuroanatomy, signalling, cognition, imaging physics and fMRI experimental design, written up as one set of notes.", repo=REPO_NI,
      graphic="jhu", demos=["hrf", "relax"]),
 dict(id="uchicago-understanding-the-brain", title="Understanding the Brain: The Neurobiology of Everyday Life", provider="The University of Chicago · Coursera", tutors="Peggy Mason", status="cert", cert="uchicago", url=UCHI, outcomes=UCHICAGO, kind="syllabus",
      summary="Functional human neuroanatomy and neuronal communication, from perception to homeostasis.", graphic="rail", demos=[]),
 dict(id="yale-introduction-to-psychology", title="Introduction to Psychology", provider="Yale University · Coursera", tutors="Paul Bloom", status="cert", cert="yale", url=YALE_URL, outcomes=YALE, kind="syllabus",
      summary="An overview of the scientific study of thought and behaviour.", graphic="rail", demos=[]),
 dict(id="harvardx-mcb80-1x", title="Fundamentals of Neuroscience, Part 1: The Electrical Properties of the Neuron", provider="HarvardX · edX · MCB80.1x", status="audit", url=H1, outcomes=HARV1, kind="syllabus",
      summary="How individual neurons use electricity to transmit information.", graphic="rail", demos=["nernst"]),
 dict(id="harvardx-mcb80-2x", title="Fundamentals of Neuroscience, Part 2: Neurons and Networks", provider="HarvardX · edX · MCB80.2x", status="audit", url=H2, outcomes=HARV2, kind="syllabus",
      summary="How neurons pass signals to one another, and what simple circuits can do.", graphic="rail", demos=[]),
 dict(id="harvardx-mcb80-3x", title="Fundamentals of Neuroscience, Part 3: The Brain", provider="HarvardX · edX · MCB80.3x", status="audit", url=H3, outcomes=HARV3, kind="syllabus",
      summary="How the subsystems of the brain turn information into thought and action.", graphic="rail", demos=[]),
 dict(id="epflx-neuronal-dynamics", title="Neuronal Dynamics", provider="EPFLx · edX · BIO465.1x", tutors="Wulfram Gerstner", status="todo", url="https://lcnwww.epfl.ch/gerstner/NeuronalDynamics-MOOCall.html", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
 dict(id="epflx-neuronal-dynamics-of-cognition", title="Computational Neuroscience: Neuronal Dynamics of Cognition", provider="EPFLx · edX · BIO465.2x", tutors="Wulfram Gerstner", status="todo", url="https://lcnwww.epfl.ch/gerstner/NeuronalDynamics-MOOCall.html", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
 dict(id="jhu-neurohacking-in-r", title="Introduction to Neurohacking in R", provider="Johns Hopkins University · Coursera", status="todo", url="https://www.coursera.org/learn/neurohacking", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
 dict(id="jhu-principles-of-fmri-1", title="Principles of fMRI 1", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="todo", url="https://www.coursera.org/learn/functional-mri", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
 dict(id="jhu-principles-of-fmri-2", title="Principles of fMRI 2", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="todo", url="https://www.coursera.org/learn/functional-mri-2", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
]

READING = [
 ("Neuroscience Online: An Electronic Textbook for the Neurosciences", "UTHealth McGovern Medical School", "https://nba.uth.tmc.edu/neuroscience/s2/chapter01.html"),
 ("Neuronal Dynamics: online lectures and textbook", "W. Gerstner, W. Kistler, R. Naud, L. Paninski", "https://lcnwww.epfl.ch/gerstner/NeuronalDynamics-MOOCall.html"),
 ("Neuromatch Computational Neuroscience: project guidance", "Neuromatch Academy", "https://compneuro.neuromatch.io/projects/docs/project_guidance.html"),
]

# demo id -> (title, one line, refs)
DEMOS = {
 "nernst": ("Set the ion's battery", "Change the concentrations and watch the equilibrium potential move. Nernst equation at 37 °C.", [("w5", "The Cell Has a Battery")]),
 "lif": ("Integrate and fire", "Drive a leaky integrator with more current. Below threshold it never spikes; above it, rate rises with current.", [("w5", "Integrate-and-Fire")]),
 "hh": ("Hodgkin-Huxley spike", "Solved live with the classic squid-axon parameters. Compare how quickly m, h and n respond.", [("w5", "The Hodgkin--Huxley Equations"), ("w5", "Anatomy of a Spike")]),
 "sta": ("Recover a filter from spikes", "A synthetic neuron with a known filter is driven by white noise. More data brings the spike-triggered average closer to the truth.", [("w2", "The Spike-Triggered Average")]),
 "sdt": ("Move the decision threshold", "Two overlapping response distributions. Slide the threshold and trace the ROC curve.", [("w3", "Signal Detection Theory")]),
 "entropy": ("How much can a binary code carry?", "Entropy of a spike/no-spike code as firing probability changes.", [("w4", "Entropy: Average Information")]),
 "eigen": ("One eigenvalue, three regimes", "A single recurrent mode. Below 1 it amplifies, at 1 it integrates, above 1 it explodes.", [("w6", "Eigenvalues Determine Stability"), ("w6", "Amplification")]),
 "oja": ("Hebb explodes, Oja converges", "Both rules find the same direction in correlated input. Only Oja's keeps the weight finite.", [("w7", "Are These Rules Stable?"), ("w7", "Oja's Rule")]),
 "perceptron": ("What one neuron cannot learn", "Train a perceptron. AND and OR converge; XOR never does, however long it trains.", [("w8", "What Perceptrons Cannot Do")]),
 "td": ("Prediction error moves back in time", "Temporal difference learning over 120 trials. The error at reward shifts to the cue. Switch on omission to see the dip.", [("w8", "Temporal Difference Learning"), ("w8", "Dopamine")]),
 "hrf": ("From stimulus to BOLD", "Convolve a design with a canonical double-gamma response. Compare block and event-related designs.", [("ni", "The Haemodynamic Response Function"), ("ni", "The Block Design"), ("ni", "The Event-Related Design")]),
 "relax": ("T1 and T2 relaxation", "The same spins, resolved along two axes. Move each time constant independently.", [("ni", "Two Relaxations")]),
}
SCALE_DEMOS = {"molecules": ["nernst"], "neurons": ["hh", "sta"], "networks": ["oja", "eigen"], "brain": ["hrf"], "cognition": ["sdt", "td"], "disease": []}

# Own figures: file, caption, doc, section
FIGS = [
 ("w2-02_raster_psth", "Raster plot and PSTH", "w2", "A First Look at the Code"),
 ("w2-07_ln_model", "The linear-nonlinear model", "w2", "The Linear--Nonlinear Model"),
 ("w2-09_sta_geometry", "The STA, geometrically", "w2", "The Spike-Triggered Average"),
 ("w2-13_poisson", "Poisson distribution at three rates", "w2", "From Coin Flips"),
 ("w3-13_evidence_walk", "Evidence accumulating to a bound", "w3", "Accumulating Evidence Over Time"),
 ("w3-16_ml_vs_map", "Maximum likelihood vs MAP", "w3", "Maximum a Posteriori"),
 ("w7-z2_pca_rules", "Learning rules, simulated", "w7", "What Does Hebbian Learning Actually Do?"),
 ("w7-z5_competitive", "Competitive learning on three blobs", "w7", "The Competitive Learning Algorithm"),
 ("w7-z7_em", "EM from a deliberately poor start", "w7", "EM in Action"),
 ("w7-z11_pca_vs_sparse", "PCA vs sparse coding", "w7", "What the Network Learns"),
 ("w8-y2_xor", "Why XOR defeats a perceptron", "w8", "What Perceptrons Cannot Do"),
 ("w8-y4_backprop", "Backpropagation on XOR", "w8", "Learning Multilayer Networks"),
 ("w8-y6_shift", "Prediction error across 140 trials", "w8", "Does It Work?"),
 ("w8-y9_actor_critic", "Actor-critic on the barn task", "w8", "Actor--Critic Learning"),
]
AD_FIGS = [
 ("ad-16_disruption_index", "Integrated disruption index", "#integrated-disruption-index"),
 ("ad-30_pseudotime_umap_ad", "OPC to oligodendrocyte pseudotime", "#opc--oligodendrocyte-maturation-is-arrested"),
 ("ad-32_seaad_myelin_oligo", "External validation against SEA-AD", "#external-validation-against-sea-ad"),
 ("ad-20_transcriptional_noise", "Transcriptional noise", "#transcriptional-noise"),
]

BOOK_BASE = "https://nba.uth.tmc.edu/neuroscience/"
BOOK = {
 "molecules": [("s1/chapter02.html", "S1 Ch 2", "Ionic mechanisms of action potentials"), ("s1/chapter05.html", "S1 Ch 5", "Mechanisms of neurotransmitter release"), ("s1/chapter11.html", "S1 Ch 11", "Acetylcholine neurotransmission"), ("s1/chapter12.html", "S1 Ch 12", "Biogenic amine neurotransmitters"), ("s1/chapter13.html", "S1 Ch 13", "Amino acid neurotransmitters")],
 "neurons": [("s1/introduction.html", "S1 Intro", "Introduction to neurons and neural networks"), ("s1/chapter01.html", "S1 Ch 1", "Resting potentials and action potentials"), ("s1/chapter03.html", "S1 Ch 3", "Propagation of action potentials"), ("s1/chapter08.html", "S1 Ch 8", "Organization of cell types")],
 "networks": [("s1/chapter06.html", "S1 Ch 6", "Synaptic transmission in the CNS"), ("s1/chapter07.html", "S1 Ch 7", "Synaptic plasticity"), ("s1/chapter09.html", "S1 Ch 9", "Synapse formation, survival and elimination")],
 "brain": [("s2/chapter01.html", "S2 Ch 1", "Overview of the nervous system"), ("s2/chapter15.html", "S2 Ch 15", "Visual processing: cortical pathways"), ("s3/chapter03.html", "S3 Ch 3", "Motor cortex"), ("s3/chapter05.html", "S3 Ch 5", "Cerebellum"), ("s4/chapter11.html", "S4 Ch 11", "Blood brain barrier and cerebral metabolism")],
 "cognition": [("s3/chapter04.html", "S3 Ch 4", "Basal ganglia"), ("s4/chapter05.html", "S4 Ch 5", "Limbic system: hippocampus"), ("s4/chapter07.html", "S4 Ch 7", "Learning and memory"), ("s4/chapter08.html", "S4 Ch 8", "Higher cortical functions: language"), ("s4/chapter09.html", "S4 Ch 9", "Association and executive processing")],
 "disease": [("s4/chapter10.html", "S4 Ch 10", "CNS aging and Alzheimer's disease"), ("s4/chapter12.html", "S4 Ch 12", "Neurotransmitter and cell death"), ("s1/chapter15.html", "S1 Ch 15", "Genetics and neuronal disease"), ("s3/chapter06.html", "S3 Ch 6", "Disorders of the motor system")],
}
