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
    "cam_dm": ("The Neuropsychology of Decision Making", "University of Cambridge", "12 Nov 2026", "2026-11-12",
               "certificates/cambridge-decision-making", "https://coursera.org/verify/DHLJY1GK73T3"),
    "cam_em": ("The Psychology of Emotions: An Introduction to Embodied Cognition", "University of Cambridge", "13 Nov 2026", "2026-11-13",
               "certificates/cambridge-emotions", "https://coursera.org/verify/SHSP2TR2NRWS"),
    "nh": ("Introduction to Neurohacking in R", "Johns Hopkins University", "13 Nov 2026", "2026-11-13",
           "certificates/jhu-neurohacking", "https://coursera.org/verify/B8TCDT85UFX5"),
    "fmri2": ("Principles of fMRI 2", "Johns Hopkins University", "13 Nov 2026", "2026-11-13",
              "certificates/jhu-fmri-2", "https://coursera.org/verify/0UPYX3T9B2PO"),
    "spec": ("Neuroscience and Neuroimaging Specialization (four courses)", "Johns Hopkins University", "13 Nov 2026", "2026-11-13",
             "certificates/jhu-neuroimaging-specialization", "https://coursera.org/verify/specialization/V07M7VQV6RBT"),
    "fmri1": ("Principles of fMRI 1", "Johns Hopkins University", "11 Nov 2026", "2026-11-11",
              "certificates/jhu-fmri-1", "https://coursera.org/verify/GU355TIR3Y3T"),
    "dnaseq": ("Algorithms for DNA Sequencing", "Johns Hopkins University", "2 Mar 2023", "2023-03-02",
               "certificates/jhu-dna-sequencing", "https://coursera.org/verify/6WHNXBPM9ADE"),
    "bigdata": ("Big Data, Genes, and Medicine", "The State University of New York", "23 Feb 2023", "2023-02-23",
                "certificates/suny-big-data-genes-medicine", "https://coursera.org/verify/5M94FLSV24AV"),
    "drug": ("Drug Discovery", "University of California San Diego", "7 Jun 2020", "2020-06-07",
             "certificates/ucsd-drug-discovery", "https://coursera.org/verify/BX6GZN83E8ZD"),
    "ph125": ("Data Science: Building Machine Learning Models", "HarvardX · edX", "9 Jun 2026", "2026-06-09",
              None, "https://courses.edx.org/certificates/5336d0f75ab34976a54176ceaddf48c9"),
    "gut": ("Gut Check: Exploring Your Microbiome", "University of Colorado Boulder and University of California San Diego", "3 Jan 2024", "2024-01-03",
            "certificates/ucsd-gut-microbiome", "https://coursera.org/verify/MAYNZFYME84M"),
    "pygen": ("Python for Genomic Data Science", "Johns Hopkins University", "23 Feb 2023", "2023-02-23",
              "certificates/jhu-python-genomics", "https://coursera.org/verify/6KMNE3VGRSRZ"),
    "permed": ("Personalised Medicine from a Nordic Perspective", "University of Copenhagen and University of Iceland", "21 Feb 2023", "2023-02-21",
               "certificates/copenhagen-personalised-medicine", "https://coursera.org/verify/XU2AGBX8XXV4"),
    "galaxy": ("Genomic Data Science with Galaxy", "Johns Hopkins University", "4 Jul 2021", "2021-07-04",
               "certificates/jhu-galaxy", "https://coursera.org/verify/HMU9G7PVXRV7"),
    "gentech": ("Introduction to Genomic Technologies", "Johns Hopkins University", "13 Jun 2021", "2021-06-13",
                "certificates/jhu-genomic-technologies", "https://coursera.org/verify/CU83YTNHGRNA"),
    "covid": ("COVID19 Data Analysis Using Python (guided project)", "Coursera Project Network", "8 Jan 2021", "2021-01-08",
              "certificates/coursera-covid19-python", "https://coursera.org/verify/UHPRLKTYMFTM"),
    "biotech": ("Industrial Biotechnology", "University of Manchester", "22 Jun 2020", "2020-06-22",
                "certificates/manchester-industrial-biotechnology", "https://coursera.org/verify/KXTX6VU3ANZ9"),
    "stem": ("The Science of Stem Cells", "American Museum of Natural History", "6 Jun 2020", "2020-06-06",
             "certificates/amnh-stem-cells", "https://coursera.org/verify/VP7RHFMX5RMZ"),
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
HARV1 = [("neurons", "Lessons", "Resting potential"), ("neurons", "Lessons", "Passive membrane properties"), ("neurons", "Lessons", "Action potentials"),
         ("neurons", "Lessons", "Action potential propagation"), ("neurons", "Lessons", "DIY labs")]
HARV2 = [("molecules", "Lessons", "The synapse"), ("networks", "Lessons", "Excitation and inhibition"), ("networks", "Lessons", "Small circuits"),
         ("molecules", "Lessons", "Neuromodulation"), ("networks", "Lessons", "Potentiation and depression")]
HARV3 = [("brain", "Lessons", "Vision"), ("brain", "Lessons", "Audition"), ("brain", "Lessons", "Touch, taste, smell and the remaining senses"),
         ("brain", "Lessons", "Movement and action"), ("brain", "Lessons", "Subcortical brain areas"), ("brain", "Lessons", "Brain anatomy")]

AD_FINDINGS = [
 ("disease", "Original research", "The oligodendrocyte lineage is the main axis of disruption in this tissue, rising from 19.7% to 36.0% of cells.", "#biological-conclusions"),
 ("disease", "Original research", "Pathology is spatially zoned: AD-hot zones are about 58% oligodendrocyte, Preserved zones about 15%.", "#milestone-9--spatial-ad-zoning"),
 ("disease", "Original research", "The myelin programme fragments rather than simply declining; different myelin genes move in opposite directions.", "#the-myelin-module-fragments--the-central-oligodendrocyte-result"),
 ("disease", "Original research", "Core oligodendrocyte claims replicate in SEA-AD, an independent cohort (MAG, FDR 0.019).", "#external-validation-against-sea-ad"),
 ("disease", "Original research", "Limits stated up front: one section per condition, and a detection gap (median 28 vs 69 genes per cell) that confounds cross-section differential expression.", "#limitations"),
]

M = "Official course modules"
FMRI1 = [("brain", M, "Introduction to fMRI, data acquisition and reconstruction"),
         ("brain", M, "The fMRI signal, experimental design and pre-processing"),
         ("brain", M, "The General Linear Model"),
         ("brain", M, "Group-level analysis and the multiple comparison problem")]
FMRI2 = [("cognition", M, "Psychological and behavioural inference, and advanced experimental design"),
         ("brain", M, "Advanced experimental design and advanced GLM modelling"),
         ("brain", M, "Brain connectivity"),
         ("brain", M, "Multi-voxel pattern analysis")]
NEUROHACK = [("brain", M, "Introduction"), ("brain", M, "Neuroimaging: formats and visualization"),
             ("brain", M, "Image processing"), ("brain", M, "Extended image processing")]
CAM_DM_URL = "https://www.coursera.org/learn/neuropsychology-of-decision-making"
CAM_DM = [("brain", M, "Introduction to neuroanatomy and neurodevelopment"),
          ("brain", M, "The importance of the prefrontal cortex"),
          ("molecules", M, "Neurotransmitters, neurophysiology and decision networks"),
          ("cognition", M, "Decision making styles and the role of childhood experiences"),
          ("cognition", M, "Decision making deficits")]
CAM_EM_URL = "https://www.coursera.org/learn/the-psychology-of-emotions-an-introduction-to-embodied-cognition"
CAM_EM = [("cognition", M, "What is cognitive psychology?"), ("cognition", M, "How we feel emotions"),
          ("cognition", M, "How do we study emotions?"),
          ("cognition", M, "How do we recognise others' emotional facial expressions?"),
          ("cognition", M, "Is it always easy to understand others' emotions?")]

EPFL2_URL = "https://www.edx.org/learn/neuroscience/ecole-polytechnique-federale-de-lausanne-computational-neuroscience-neuronal-dynamics-of-cognition"
W = "Course contents by week"
EPFL2 = [("networks", W, "Associative memory and the Hopfield model"), ("networks", W, "Attractor networks and spiking neurons"),
         ("networks", W, "Neuronal populations and mean-field theory"), ("brain", W, "Perception and cortical field models"),
         ("cognition", W, "Decision making and competitive dynamics"), ("networks", W, "Synaptic plasticity and learning")]

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
 dict(id="epflx-neuronal-dynamics-of-cognition", title="Computational Neuroscience: Neuronal Dynamics of Cognition", provider="EPFLx · edX · BIO465.2x", tutors="Wulfram Gerstner", status="audit", url=EPFL2_URL, outcomes=EPFL2, kind="syllabus",
      summary="Six weeks on how networks of neurons give rise to memory, perception and decisions.", graphic="rail", demos=[]),
 dict(id="jhu-neurohacking-in-r", title="Introduction to Neurohacking in R", provider="Johns Hopkins University · Coursera", tutors="Elizabeth Sweeney, Ciprian Crainiceanu, John Muschelli", status="cert", cert="nh", url="https://www.coursera.org/learn/neurohacking", outcomes=NEUROHACK, kind="syllabus",
      summary="Reading, visualising and processing structural brain images in R.", graphic="rail", demos=[]),
 dict(id="jhu-principles-of-fmri-1", title="Principles of fMRI 1", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="cert", cert="fmri1", url="https://www.coursera.org/learn/functional-mri", outcomes=FMRI1, kind="syllabus",
      summary="How fMRI data are acquired, pre-processed and analysed with the General Linear Model.", graphic="rail", demos=[]),
 dict(id="jhu-principles-of-fmri-2", title="Principles of fMRI 2", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="cert", cert="fmri2", url="https://www.coursera.org/learn/functional-mri-2", outcomes=FMRI2, kind="syllabus",
      summary="Advanced design and modelling, brain connectivity and multi-voxel pattern analysis.", graphic="rail", demos=[]),
 dict(id="cambridge-neuropsychology-of-decision-making", title="The Neuropsychology of Decision Making", provider="University of Cambridge · Coursera", tutors="Stacey Bedwell", status="cert", cert="cam_dm", url=CAM_DM_URL, outcomes=CAM_DM, kind="syllabus",
      summary="The neuroanatomy, prefrontal function and neurochemistry behind how decisions are made.", graphic="rail", demos=[]),
 dict(id="cambridge-psychology-of-emotions", title="The Psychology of Emotions: An Introduction to Embodied Cognition", provider="University of Cambridge · Coursera", tutors="Giulia Mangiaracina", status="cert", cert="cam_em", url=CAM_EM_URL, outcomes=CAM_EM, kind="syllabus",
      summary="How emotions are felt, studied and recognised in others, from a cognitive psychology view.", graphic="rail", demos=[]),
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

# ---- skills, for the certificates page
# key, name, colour variable
MAJORS = [("neuro", "Neuroscience", "neurons"), ("imaging", "Neuroimaging", "brain"), ("psych", "Psychology and cognition", "cognition"),
          ("ml", "Machine learning and modelling", "networks"), ("data", "Statistics, data and programming", "molecules"),
          ("bio", "Genomics and biomedicine", "disease")]
SKILL_MAJOR = {
 "neuro": ["Neurology", "Anatomy", "Physiology", "Sensory Systems Analysis", "Blood Pressure", "Computational Neuroscience", "Network Model", "Complex Networks", "Electronic Circuits", "Neurophysiology", "Electrophysiology", "Biophysics", "Synaptic Transmission", "Neural Circuits", "Neuromodulation", "Synaptic Plasticity", "Neuroanatomy", "Motor Systems", "Dynamical Systems", "Associative Memory Models"],
 "imaging": ["Magnetic Resonance Imaging", "Medical Imaging", "Image Analysis", "Image Quality", "Scientific Visualization", "Software Visualization", "Medical Terminology"],
 "psych": ["Psychology", "Learning Theory", "Human Learning", "Mental Health Diseases and Disorders", "Psychotherapy", "Cognitive Behavioral Therapy", "Human Development", "Child Development", "Non-Verbal Communication", "Critical Thinking", "Problem Solving"],
 "ml": ["Machine Learning", "Machine Learning Algorithms", "Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Artificial Neural Networks", "Recurrent Neural Networks (RNNs)", "Convolutional Neural Networks", "Deep Learning", "Artificial Intelligence", "Mathematical Modeling", "Mathematics", "Predictive Modeling", "Classification Algorithms", "Model Evaluation", "Predictive Analytics", "Principal Component Analysis", "Dimensionality Reduction", "Recommender Systems", "Forecasting", "PyTorch", "Keras", "TensorFlow", "Autoencoders", "Transfer Learning", "Transformer Models", "Linear Regression", "Logistic Regression", "Loss Functions", "Cross-Validation", "Regularization", "Backpropagation", "Gradient Descent", "Tensors", "Time Series", "Image Classification"],
 "data": ["Statistical Analysis", "Statistics", "Statistical Modeling", "Data Analysis", "Data Preprocessing", "Data Cleansing", "Data Visualization", "Data Manipulation", "Data Transformation", "Data Import/Export", "Data Processing", "Data Integration", "Data Quality", "Correlation Analysis", "Research Design", "Research Methodologies", "Research", "R Programming", "Python Programming", "Seaborn", "NumPy", "Pandas", "Package and Software Management", "Data Structures", "Algorithms", "Computer Programming", "Programming Principles", "Code Reusability", "File I/O", "Data Science", "Computer Science", "Software Engineering", "Big Data", "Application Frameworks", "Computing Platforms", "Data Analysis Software", "Software Installation", "Data-Driven Decision-Making"],
 "bio": ["Bioinformatics", "Molecular Biology", "Biology", "Cell Biology", "Microbiology", "Immunology", "Nutrition and Diet", "Precision Medicine", "Medical Science and Research", "Clinical Research", "Healthcare Ethics", "Risk Analysis", "Patient-centered Care", "Health Care Procedure and Regulation", "Patient Communication", "Healthcare Industry Knowledge", "Health Systems", "Biotechnology", "Pharmaceuticals", "Drug Development", "Pharmacology", "Clinical Trials", "Process Engineering", "Sustainable Technologies", "Manufacturing and Production", "Scalability"],
}
# certificate key -> major, one-line summary, skills as listed on the course page, official page
CERT_META = {
 "uw": dict(major="neuro", url="https://www.coursera.org/learn/computational-neuroscience", summary="How neurons encode and decode information, and how networks compute and learn.",
            skills=["Network Model", "Mathematical Modeling", "Reinforcement Learning", "Supervised Learning", "Artificial Neural Networks", "Recurrent Neural Networks (RNNs)", "Machine Learning Algorithms"]),
 "uchicago": dict(major="neuro", url=UCHI, summary="Functional neuroanatomy, perception, movement and homeostasis.",
                  skills=["Anatomy", "Neurology", "Physiology", "Sensory Systems Analysis", "Biology", "Blood Pressure"]),
 "cam_dm": dict(major="neuro", url=CAM_DM_URL, summary="Prefrontal cortex, neurotransmitters and the networks behind decisions.",
                skills=["Neurology", "Anatomy", "Physiology", "Psychology", "Biology", "Mental Health Diseases and Disorders"]),
 "jhu": dict(major="imaging", url="https://www.coursera.org/learn/neuroscience-neuroimaging", summary="Structural and functional neuroanatomy, imaging methods and experimental design.",
             skills=["Magnetic Resonance Imaging", "Medical Imaging", "Anatomy", "Research Design", "Medical Terminology"]),
 "nh": dict(major="imaging", url="https://www.coursera.org/learn/neurohacking", summary="Reading, visualising and processing structural brain images in R.",
            skills=["Image Analysis", "Medical Imaging", "R Programming", "Data Preprocessing", "Scientific Visualization", "Image Quality", "Neurology", "Data Manipulation", "Data Transformation", "Data Import/Export", "Software Visualization", "Package and Software Management"]),
 "fmri1": dict(major="imaging", url="https://www.coursera.org/learn/functional-mri", summary="How fMRI data are acquired, pre-processed and analysed with the General Linear Model.",
               skills=["Magnetic Resonance Imaging", "Statistical Analysis", "Statistical Modeling", "Data Analysis", "Data Preprocessing", "Research Design", "Statistics"]),
 "fmri2": dict(major="imaging", url="https://www.coursera.org/learn/functional-mri-2", summary="Advanced fMRI design and modelling, connectivity and multi-voxel pattern analysis.",
               skills=["Magnetic Resonance Imaging", "Statistical Modeling", "Statistical Analysis", "Data Analysis", "Psychology"]),
 "spec": dict(major="imaging", url="https://www.coursera.org/specializations/computational-neuroscience", summary="All four Johns Hopkins courses: fundamental neuroscience, fMRI 1 and 2, and neurohacking in R.",
              skills=["Magnetic Resonance Imaging", "Medical Imaging", "Image Analysis", "Statistical Analysis", "Research Design", "Anatomy", "Neurology", "Data Preprocessing"]),
 "yale": dict(major="psych", url=YALE_URL, summary="The scientific study of thought and behaviour, from development to mental illness.",
              skills=["Psychology", "Learning Theory", "Human Learning", "Human Development", "Child Development", "Mental Health Diseases and Disorders", "Psychotherapy", "Cognitive Behavioral Therapy", "Critical Thinking", "Problem Solving"]),
 "cam_em": dict(major="psych", url=CAM_EM_URL, summary="How emotions are felt, studied and recognised in other people.",
                skills=["Psychology", "Research Methodologies", "Research", "Non-Verbal Communication"]),
 "ph125": dict(major="ml", url="https://www.edx.org/learn/machine-learning/harvard-university-data-science-machine-learning", summary="Cross-validation, regularisation, common algorithms and a recommendation system, in R.",
               skills=["Machine Learning", "Cross-Validation", "Regularization", "Classification Algorithms", "Machine Learning Algorithms", "Principal Component Analysis", "Recommender Systems", "Model Evaluation", "Forecasting", "R Programming", "Data Science", "Algorithms"]),
 "covid": dict(major="data", url="https://www.coursera.org/projects/covid19-data-analysis-using-python", summary="A guided project: cleaning, merging and correlating public COVID-19 datasets.",
               skills=["Python Programming", "Data Analysis", "Data Visualization", "Statistical Analysis", "Correlation Analysis", "Data Preprocessing", "Data Cleansing", "Data Integration", "Statistics", "Seaborn"]),
 "gut": dict(major="bio", url="https://www.coursera.org/learn/microbiome", summary="The human gut microbiome, how it is studied and what it means for health.",
             skills=["Microbiology", "Immunology", "Nutrition and Diet", "Data Analysis"]),
 "pygen": dict(major="bio", url="https://www.coursera.org/learn/python-genomics", summary="Python programming applied to sequence data.",
               skills=["Bioinformatics", "Python Programming", "Data Structures", "Computer Programming", "Programming Principles", "Code Reusability", "File I/O"]),
 "permed": dict(major="bio", url="https://www.coursera.org/learn/personalised-medicine-from-a-nordic-perspective", summary="Biomarkers, genetics and omics in personalised medicine, with its evidence, ethics and communication.",
                skills=["Precision Medicine", "Medical Science and Research", "Clinical Research", "Healthcare Ethics", "Data Science", "Risk Analysis", "Patient-centered Care", "Patient Communication", "Health Systems", "Healthcare Industry Knowledge", "Health Care Procedure and Regulation", "Data-Driven Decision-Making"]),
 "galaxy": dict(major="bio", url=None, summary="Reproducible genomic analysis on the Galaxy platform.",
                skills=["Bioinformatics", "Data Analysis", "Big Data", "Data Quality", "Data Analysis Software", "Application Frameworks", "Computing Platforms", "Software Installation"]),
 "gentech": dict(major="bio", url="https://www.coursera.org/learn/introduction-genomics", summary="The measurement, computing and data science behind modern genomics.",
                 skills=["Bioinformatics", "Molecular Biology", "Biology", "Statistical Analysis", "Data Analysis", "Algorithms", "Statistics", "Correlation Analysis", "Data Processing", "Data Science", "Computer Science", "Software Engineering"]),
 "dnaseq": dict(major="bio", url="https://www.coursera.org/learn/dna-sequencing", summary="String matching, indexing and assembly algorithms for sequencing reads, in Python.",
                skills=["Bioinformatics", "Algorithms", "Data Structures", "Python Programming", "Data Analysis"]),
 "bigdata": dict(major="bio", url="https://www.coursera.org/learn/data-genes-medicine", summary="Finding differentially expressed genes and predicting disease from expression data, in R.",
                 skills=["Bioinformatics", "Predictive Modeling", "Classification Algorithms", "R Programming", "Big Data", "Model Evaluation", "Data Preprocessing", "Data Cleansing", "Predictive Analytics", "Medical Science and Research"]),
 "drug": dict(major="bio", url="https://www.coursera.org/learn/drug-discovery", summary="How a drug moves from target and compound selection to preclinical studies and delivery.",
              skills=["Drug Development", "Pharmacology", "Clinical Trials", "Pharmaceuticals", "Biotechnology"]),
 "biotech": dict(major="bio", url="https://www.coursera.org/learn/industrial-biotech", summary="Enzyme engineering, synthetic biology and bioprocessing, with industrial case studies.",
                 skills=["Biotechnology", "Pharmaceuticals", "Process Engineering", "Sustainable Technologies", "Manufacturing and Production", "Scalability"]),
 "stem": dict(major="bio", url="https://www.coursera.org/learn/stem-cells", summary="What stem cells are, and how they are used to study and treat disease.",
              skills=["Cell Biology", "Biology", "Precision Medicine", "Medical Science and Research", "Healthcare Ethics"]),
}
IBM = "IBM · edX"
# Audited courses: lessons as named by the course, skills as listed on the course page where it lists any
AUDITS = [
 dict(title="Fundamentals of Neuroscience, Part 1: The Electrical Properties of the Neuron", provider="HarvardX · edX · MCB80.1x", major="neuro", page="harvardx-mcb80-1x", url=H1, lessons_label="Lessons",
      lessons=["Resting potential", "Passive membrane properties", "Action potentials", "Action potential propagation", "DIY labs"], skills=["Neurophysiology", "Electrophysiology", "Biophysics", "Physiology", "Biology"]),
 dict(title="Fundamentals of Neuroscience, Part 2: Neurons and Networks", provider="HarvardX · edX · MCB80.2x", major="neuro", page="harvardx-mcb80-2x", url=H2, lessons_label="Lessons",
      lessons=["The synapse", "Excitation and inhibition", "Small circuits", "Neuromodulation", "Potentiation and depression"], skills=["Synaptic Transmission", "Neural Circuits", "Neuromodulation", "Synaptic Plasticity", "Neurophysiology", "Complex Networks", "Electronic Circuits"]),
 dict(title="Fundamentals of Neuroscience, Part 3: The Brain", provider="HarvardX · edX · MCB80.3x", major="neuro", page="harvardx-mcb80-3x", url=H3, lessons_label="Lessons",
      lessons=["Vision", "Audition", "Touch, taste, smell and the remaining senses", "Movement and action", "Subcortical brain areas", "Brain anatomy"], skills=["Neuroanatomy", "Sensory Systems Analysis", "Motor Systems", "Physiology", "Anatomy"]),
 dict(title="Computational Neuroscience: Neuronal Dynamics of Cognition", provider="EPFLx · edX · BIO465.2x", major="neuro", page="epflx-neuronal-dynamics-of-cognition", url=EPFL2_URL, lessons_label="Weeks",
      lessons=[o[2] for o in EPFL2], skills=["Computational Neuroscience", "Network Model", "Mathematical Modeling", "Dynamical Systems", "Associative Memory Models", "Synaptic Plasticity", "Mathematics"]),
 dict(title="Deep Learning Fundamentals with Keras", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-deep-learning-fundamentals-with-keras", lessons_label="Modules",
      lessons=["Introduction to deep learning: biological and artificial neural networks, forward propagation", "Artificial neural networks: gradient descent, backpropagation, vanishing gradient, activation functions",
               "Deep learning libraries: regression and classification models with Keras", "Deep learning models: shallow and deep networks, convolutional and recurrent networks, autoencoders"],
      skills=["Deep Learning", "Keras", "Artificial Neural Networks", "Backpropagation", "Gradient Descent", "Convolutional Neural Networks", "Recurrent Neural Networks (RNNs)", "Autoencoders", "Artificial Intelligence", "Data Science"]),
 dict(title="PyTorch Basics for Machine Learning", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/pytorch/ibm-pytorch-basics-for-machine-learning", lessons_label="What the course covers",
      lessons=["Build a machine learning pipeline in PyTorch", "Train models in PyTorch", "Load large datasets", "Use NumPy and Pandas with PyTorch"],
      skills=["PyTorch", "Machine Learning", "Tensors", "Gradient Descent", "Linear Regression", "Logistic Regression", "Loss Functions", "Python Programming", "NumPy", "Pandas"]),
 dict(title="Deep Learning with Python and PyTorch", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-deep-learning-with-python-and-pytorch", lessons_label="What the course covers",
      lessons=["Deep neural networks and related machine learning methods", "Build and train deep neural networks using PyTorch", "Build deep learning pipelines"],
      skills=["PyTorch", "Deep Learning", "Convolutional Neural Networks", "Artificial Neural Networks", "Backpropagation", "Autoencoders", "Transfer Learning", "Dimensionality Reduction", "Principal Component Analysis", "Python Programming"]),
 dict(title="Deep Learning with TensorFlow and Keras", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-deep-learning-with-tensorflow-and-keras", lessons_label="What the course covers",
      lessons=["Custom layers and models in Keras with TensorFlow 2.x", "Advanced convolutional neural networks", "Transformer models for sequential data and time series", "Unsupervised learning, deep Q-networks and reinforcement learning"],
      skills=["TensorFlow", "Keras", "Convolutional Neural Networks", "Transformer Models", "Time Series", "Reinforcement Learning", "Unsupervised Learning", "Transfer Learning", "Autoencoders", "Deep Learning"]),
 dict(title="Applied Deep Learning Capstone Project", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-applied-deep-learning-capstone-project", lessons_label="What the course covers",
      lessons=["Choose a deep learning method for a given problem", "Build a deep learning model for a real problem", "Create a deep learning pipeline", "Improve models using real data", "Present the outcomes of a deep learning project"],
      skills=["Deep Learning", "PyTorch", "Keras", "Image Classification", "Model Evaluation", "Data Preprocessing"]),
]

# ---- toolkit, for the home page. (name, colour, "used" in my own projects | "course" for audited coursework only)
TOOLKIT = [
 ("Languages", [("Python", "#3776AB", "used"), ("R", "#276DC3", "used"), ("Bash", "#3E8E2C", "used"), ("LaTeX", "#0F6E6E", "used")]),
 ("Data and statistics", [("pandas", "#3B2A8C", "used"), ("NumPy", "#4D77CF", "used"), ("SciPy", "#0054A6", "used"), ("statsmodels", "#3F4F75", "used"),
                          ("tidyverse", "#2C3E66", "used"), ("ggplot2", "#4F7CAC", "used"), ("vegan", "#4E7D2B", "used")]),
 ("Machine learning", [("scikit-learn", "#C96A00", "used"), ("PyTorch", "#EE4C2C", "used"), ("Keras", "#D00000", "course"), ("TensorFlow", "#E65C00", "course")]),
 ("Omics", [("Scanpy", "#6A4C93", "used"), ("Squidpy", "#8A3F7C", "used"), ("AnnData", "#2F7D7B", "used"), ("GSEApy", "#8D5A2B", "used"),
            ("Biopython", "#3A7CA5", "used"), ("MaAsLin3", "#7A5C00", "used"), ("MetaPhlAn", "#A8326A", "used"), ("HUMAnN", "#8D2C2C", "used")]),
 ("Workflow", [("Git", "#D9411E", "used"), ("Jupyter", "#C75B12", "used"), ("Docker", "#1D7FC4", "used"), ("Nextflow", "#1E9E73", "used"), ("Snakemake", "#03627A", "used"), ("pytest", "#0A7FB0", "used")]),
]
TOOLKIT_METHODS = [
 ("Spatial and single-cell transcriptomics", "Xenium and Visium, clustering and annotation, differential expression, spatial statistics, ligand–receptor analysis"),
 ("Metagenomics", "shotgun profiling, factorial differential abundance, PERMANOVA"),
 ("Statistical genetics", "gene-burden tests, LD score regression, polygenic scores"),
 ("Neuroscience", "neural encoding and decoding models, neuron and network simulation, fMRI design and analysis"),
]

# title, role, status, methods
AD_PROJECTS = [
 ("Spatial transcriptomics of human Alzheimer's cortex", "Independent project", "2026, public repository and technical report",
  ["10x Xenium", "Cell-type annotation", "Spatial niche classifiers", "Spatially variable genes", "Ligand–receptor analysis", "Transcriptional noise", "Cell-type vulnerability index", "Validation against the SEA-AD atlas"]),
 ("Multi-omics integration of published Alzheimer's disease datasets", "Independent project", "2026",
  ["Genomic, transcriptomic and proteomic data", "MOFA+", "DIABLO", "sPLS", "Transcript–protein concordance"]),
 ("Quercetin in a zebrafish model of Alzheimer's disease", "Bachelor's project, Amity University", "BSc, 2018 to 2021",
  ["Zebrafish disease model", "Behavioural analysis", "Biochemical analysis", "Molecular docking of quercetin compounds with acetylcholinesterase"]),
 ("GPCR-targeted therapeutic strategies in neurodegenerative disease", "Author of the review", "Ethical Edufabrica, 2020",
  ["Literature review", "GPCR signalling", "Therapeutic strategies"]),
]
OMICS_PROJECTS = [
 ("Westernized diets exacerbate tumorigenesis by upregulating H₂S-producing bacteria", "Co-first author", "Manuscript in preparation",
  ["Reference-based metagenomic profiling", "Assembly-based metagenomics", "Sulfur and fatty-acid metabolism analysis", "16S rRNA amplicon analysis", "Protein structure analysis", "Variant analysis", "Metabolomics", "Metabolic modelling", "HPC", "Snakemake", "Nextflow"]),
 ("Host-specific divergence in motility and sulfur metabolism across 2,000 Desulfovibrio genomes", "First author", "Manuscript in preparation",
  ["Curation of public MAGs and isolate genomes", "Hybrid assembly", "Reference database expansion", "Interactive analysis tool", "Sulfur-metabolism, toxin and flagellar genes", "Gene and pathway analysis", "Protein structure analysis", "Genome-scale metabolic modelling", "Machine-learning models", "Pipeline development", "HPC and GPU computing", "Snakemake", "Nextflow"]),
 ("An expanded flagellin repertoire in a mouse-restricted Desulfovibrio associated with XIAP deficiency", "Co-author", "Manuscript in preparation",
  ["Reference-based metagenomic profiling", "Assembly-based metagenomics", "16S rRNA amplicon analysis", "Flagellar gene and pathway analysis", "Pipeline development", "Nextflow"]),
 ("Gut microbiome of the small intestine and colon in mice, and a search for bacterial choline acetyltransferase", "Analysis and report", "Written report, 2026",
  ["Shotgun metagenomics", "Taxonomic and functional profiling", "Diversity statistics", "Metagenome assembly and gene catalogue", "Metagenomic species pangenomes", "Metagenome-assembled genomes", "Sequence and protein-domain search", "Structural homology search", "Nextflow"]),
 ("Methylation motifs of Veillonella parvula", "Exploratory project", "Not completed",
  ["Nanopore assembly and analysis", "Illumina and hybrid assembly", "Prophage detection", "Methylation and motif detection", "Algorithm optimisation", "HPC and GPU computing"]),
]

# ---- summary map and grouping, for the certificates page
# Each area: key, name, colour variable, where it comes from, branches (key, name, source note, leaves, optional link)
TREE = [
 dict(key="neuro", name="Neuroscience", col="neurons", note="Coursework, research projects and a review, 2020 to 2026", branches=[
  dict(key="fund", name="Fundamental neuroscience", leaves=["Neuroanatomy", "Neurophysiology", "Synapses and circuits", "Sensory and motor systems", "Homeostasis"]),
  dict(key="comp", name="Computational neuroscience", leaves=["Neural encoding and decoding", "Information theory", "Neuron and network models", "Plasticity and learning", "Attractor networks"]),
  dict(key="imaging", name="Neuroimaging", leaves=["MRI", "fMRI experimental design", "General Linear Model", "Connectivity", "Multi-voxel pattern analysis", "Image processing in R"]),
  dict(key="psych", name="Psychology", leaves=["Cognitive psychology", "Decision making", "Emotion", "Development and learning", "Mental health"]),
  dict(key="ad", name="Alzheimer's disease and neurodegeneration", note="Research projects and a review, 2020 to 2026", link=REPO_AD, projects_label="Projects and review",
       leaves=["Alzheimer's pathology", "Neurodegenerative diseases", "Selective cell-type vulnerability", "Spatial transcriptomics of human cortex", "Zebrafish disease model", "GPCR-targeted therapies"], projects=AD_PROJECTS),
 ]),
 dict(key="dl", name="Deep learning and machine learning", col="networks", note="MSc at Manchester, research at TUM, and certified and audited coursework", branches=[
  dict(key="ml", name="Machine learning", note="MSc and certified coursework", leaves=["Cross-validation", "Regularisation", "Dimensionality reduction", "Classification", "Recommender systems"]),
  dict(key="keras", name="Keras and TensorFlow", leaves=["Regression models", "Classification models", "Custom layers and models"]),
  dict(key="pytorch", name="PyTorch", leaves=["Neural networks", "Deep networks", "Autoencoders", "Transfer learning"]),
  dict(key="cnn", name="Convolutional networks", leaves=["Keras", "PyTorch", "Variational CNNs on sequencing signal"]),
  dict(key="tfm", name="Transformers", leaves=["Sequential data", "Time-series prediction"]),
 ]),
 dict(key="bioinf", name="Bioinformatics", col="molecules", note="MSc at Manchester, research at TUM, an independent project and certified coursework", branches=[
  dict(key="msc", name="MSc Bioinformatics and Systems Biology", note="University of Manchester, 2021 to 2022, Distinction", leaves=["Python", "R", "Bash", "Sequence and structural bioinformatics", "Genomics and phylogenetics", "Statistics and experimental design", "GWAS and rare-variant burden testing", "Protein docking", "Machine learning"]),
  dict(key="omics", name="Multi-omics", note="Research at the Technical University of Munich, 2023 to 2026. Manuscripts in preparation, with submission planned for 2027.",
       leaves=["Metagenomics", "Epigenomics", "Metaproteomics", "Metabolomics", "Multi-omics integration", "Genome-scale metabolic modelling", "Workflow development", "High-performance computing"], projects=OMICS_PROJECTS),
  dict(key="spatial", name="Spatial transcriptomics", note="Independent project, 2026", link=REPO_AD, leaves=["Xenium and Visium", "Cell-type annotation", "Spatially variable genes", "Ligand–receptor analysis"]),
  dict(key="courses", name="Genomic data science", leaves=["Sequencing algorithms", "Genomic technologies", "Python for genomics", "Galaxy workflows", "Gene-expression classification in R", "Microbiome analysis"]),
 ]),
 dict(key="biotech", name="Biotechnology", col="brain", note="BSc (Hons) Biotechnology, Amity University, 2018 to 2021, and certified coursework", branches=[
  dict(key="molbio", name="Molecular biology and genetics", note="BSc", leaves=["Genetics", "Recombinant DNA technology", "Genomics and proteomics", "Human genetics and gene therapy"]),
  dict(key="biochem", name="Biochemistry and lab techniques", note="BSc", leaves=["Biochemistry", "Enzymology", "Bioanalytical techniques", "Molecular diagnostics"]),
  dict(key="micro", name="Microbiology and immunology", note="BSc", leaves=["Microbiology", "Microbial ecology", "Immunology"]),
  dict(key="physio", name="Physiology and anatomy", note="BSc", leaves=["Animal physiology", "Human anatomy", "Developmental biology"]),
  dict(key="quant", name="Quantitative foundations", note="BSc", leaves=["Biostatistics", "Biophysics", "Bioinformatics", "Computer programming", "Database management"]),
  dict(key="applied", name="Applied biotechnology", note="BSc and courses", leaves=["Animal and plant biotechnology", "Tissue engineering", "Industrial bioprocessing", "Drug discovery", "Stem cells", "Personalised medicine"]),
 ]),
]
CERT_GROUP = {"uchicago": "neuro/fund", "uw": "neuro/comp", "jhu": "neuro/imaging", "fmri1": "neuro/imaging", "fmri2": "neuro/imaging", "nh": "neuro/imaging", "spec": "neuro/imaging",
              "yale": "neuro/psych", "cam_em": "neuro/psych", "cam_dm": "neuro/psych", "ph125": "dl/ml",
              "gentech": "bioinf/courses", "pygen": "bioinf/courses", "galaxy": "bioinf/courses", "dnaseq": "bioinf/courses", "bigdata": "bioinf/courses", "gut": "bioinf/courses", "covid": "bioinf/courses",
              "biotech": "biotech/applied", "drug": "biotech/applied", "stem": "biotech/applied", "permed": "biotech/applied"}
AUDIT_GROUP = ["neuro/fund", "neuro/fund", "neuro/fund", "neuro/comp", "dl/keras", "dl/pytorch", "dl/pytorch", "dl/keras", "dl/pytorch"]
# Module names as listed on the course pages
CERT_MODULES = {
 "uw": ["Introduction and basic neurobiology", "Neural encoding models", "Neural decoding", "Information theory and neural coding", "Computing in carbon", "Computing with networks", "Plasticity in the brain and learning", "Learning from supervision and rewards"],
 "uchicago": [o[2] for o in UCHICAGO], "yale": [o[2] for o in YALE], "cam_dm": [o[2] for o in CAM_DM], "cam_em": [o[2] for o in CAM_EM],
 "jhu": ["Structural neuroanatomy of the human brain", "Functional neuroanatomy of the human brain", "Principles and methods of neuroimaging", "Experimental design and special applications in neuroimaging"],
 "fmri1": [o[2] for o in FMRI1], "fmri2": [o[2] for o in FMRI2], "nh": [o[2] for o in NEUROHACK],
 "spec": ["Fundamental Neuroscience for Neuroimaging", "Principles of fMRI 1", "Principles of fMRI 2", "Introduction to Neurohacking in R"],
 "ph125": ["The basics of machine learning", "Cross-validation to avoid overtraining", "Several popular machine learning algorithms", "Building a recommendation system", "Regularisation"],
 "gut": ["Introduction to microbes and the human microbiome", "Studying the microbiome", "Making sense out of microbial data", "The human gut microbiome and your health", "Gut microbe-host interactions: beyond nutrition", "What's in the American Gut"],
 "permed": ["Introduction to personalised medicine", "Health information used in personalised medicine", "Biomarkers, genetics and omics", "Evidence and documentation for clinical efficacy", "Communication in personalised medicine", "Ethical, legal and social aspects"],
 "gentech": ["Overview", "Measurement technology", "Computing technology", "Data science technology"],
 "biotech": ["Enzymes, enzyme discovery and engineering", "Methods in systems and synthetic biology", "Biochemical and bioprocess engineering", "Pharmaceuticals and fine chemicals", "Case studies: bioenergy and biomaterials", "Case studies: glycoscience and biotherapeutics"],
 "stem": ["Introduction to stem cells", "Using stem cells to study disease", "Using stem cells to treat disease", "The bioethics of stem cell research and therapy"],
 "dnaseq": ["DNA sequencing, strings and matching", "Preprocessing, indexing and approximate matching", "Edit distance, assembly, overlaps", "Algorithms for assembly"],
 "bigdata": ["Genes and data", "Preparing datasets for analysis", "Finding differentially expressed genes", "Predicting diseases from genes", "Determining gene alterations", "Clustering and pathway analysis"],
 "drug": ["Pharmaceutical and biotechnology industry landscape", "Drug discovery: proteomics, genomics", "Compound selection and preclinical studies", "Fragment-based drug discovery for protein kinases", "Key concepts in drug delivery"],
}
