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
    "cam_cog": ("Introduction to Cognitive Psychology and Neuropsychology", "University of Cambridge", "11 Nov 2026", "2026-11-11",
                "certificates/cambridge-cognitive-psychology", "https://coursera.org/verify/KLZF03C12VAA"),
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
CAM_COG_URL = "https://www.coursera.org/learn/introduction-to-cognitive-psychology-and-neuropsychology"
CAM_COG = [("cognition", M, "What is cognitive psychology? History and core debates"), ("cognition", M, "How do we measure the mind? Research methods"),
           ("cognition", M, "The psychology of human language"), ("cognition", M, "Memory, perception and cross-modal interactions"),
           ("cognition", M, "Attention, consciousness and free will")]
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
      summary="An eight-week course on how neurons encode and decode information and how networks compute and learn, written up as my own LaTeX notes with working simulations.", repo=REPO_CN,
      graphic="uw", demos=["sta", "sdt", "entropy", "hh", "lif", "eigen", "oja", "perceptron", "td"]),
 dict(id="jhu-neuroimaging", title="Fundamental Neuroscience for Neuroimaging", provider="Johns Hopkins University · Coursera", tutors="Arnold Bakker", status="cert", cert="jhu", url="https://www.coursera.org/learn/neuroscience-neuroimaging", outcomes=NI, kind="notes",
      summary="The structural and functional anatomy of the human brain, and the physics, methods and experimental design behind neuroimaging.", repo=REPO_NI,
      graphic="jhu", demos=["hrf", "relax"]),
 dict(id="uchicago-understanding-the-brain", title="Understanding the Brain: The Neurobiology of Everyday Life", provider="The University of Chicago · Coursera", tutors="Peggy Mason", status="cert", cert="uchicago", url=UCHI, outcomes=UCHICAGO, kind="syllabus",
      summary="How the nervous system produces perception, movement, emotion and homeostasis in everyday life, taught through functional neuroanatomy.", graphic="rail", demos=[]),
 dict(id="yale-introduction-to-psychology", title="Introduction to Psychology", provider="Yale University · Coursera", tutors="Paul Bloom", status="cert", cert="yale", url=YALE_URL, outcomes=YALE, kind="syllabus",
      summary="A broad introduction to the scientific study of thought and behaviour, from perception, memory and development to mental illness.", graphic="rail", demos=[]),
 dict(id="harvardx-mcb80-1x", title="Fundamentals of Neuroscience, Part 1: The Electrical Properties of the Neuron", provider="HarvardX · edX · MCB80.1x", status="audit", url=H1, outcomes=HARV1, kind="syllabus",
      summary="The electrical basis of neural signalling: how ions, membranes and channels produce the resting potential and the action potential.", graphic="rail", demos=["nernst"]),
 dict(id="harvardx-mcb80-2x", title="Fundamentals of Neuroscience, Part 2: Neurons and Networks", provider="HarvardX · edX · MCB80.2x", status="audit", url=H2, outcomes=HARV2, kind="syllabus",
      summary="How neurons communicate at synapses, and how excitation, inhibition and plasticity shape what small circuits can do.", graphic="rail", demos=[]),
 dict(id="harvardx-mcb80-3x", title="Fundamentals of Neuroscience, Part 3: The Brain", provider="HarvardX · edX · MCB80.3x", status="audit", url=H3, outcomes=HARV3, kind="syllabus",
      summary="How the sensory, motor and subcortical systems of the brain turn information into perception and action.", graphic="rail", demos=[]),
 dict(id="epflx-neuronal-dynamics", title="Neuronal Dynamics", provider="EPFLx · edX · BIO465.1x", tutors="Wulfram Gerstner", status="todo", url="https://lcnwww.epfl.ch/gerstner/NeuronalDynamics-MOOCall.html", outcomes=[], kind="todo",
      summary="To be updated.", graphic=None, demos=[]),
 dict(id="epflx-neuronal-dynamics-of-cognition", title="Computational Neuroscience: Neuronal Dynamics of Cognition", provider="EPFLx · edX · BIO465.2x", tutors="Wulfram Gerstner", status="audit", url=EPFL2_URL, outcomes=EPFL2, kind="syllabus",
      summary="A six-week mathematical treatment of how networks of neurons give rise to memory, perception and decision making.", graphic="rail", demos=[]),
 dict(id="jhu-neurohacking-in-r", title="Introduction to Neurohacking in R", provider="Johns Hopkins University · Coursera", tutors="Elizabeth Sweeney, Ciprian Crainiceanu, John Muschelli", status="cert", cert="nh", url="https://www.coursera.org/learn/neurohacking", outcomes=NEUROHACK, kind="syllabus",
      summary="A practical introduction to reading, visualising and processing structural MRI data in R.", graphic="rail", demos=[]),
 dict(id="jhu-principles-of-fmri-1", title="Principles of fMRI 1", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="cert", cert="fmri1", url="https://www.coursera.org/learn/functional-mri", outcomes=FMRI1, kind="syllabus",
      summary="The foundations of fMRI: how the signal is acquired and pre-processed, and how experiments are designed and analysed with the General Linear Model.", graphic="rail", demos=[]),
 dict(id="jhu-principles-of-fmri-2", title="Principles of fMRI 2", provider="Johns Hopkins University · Coursera", tutors="Martin Lindquist, Tor Wager", status="cert", cert="fmri2", url="https://www.coursera.org/learn/functional-mri-2", outcomes=FMRI2, kind="syllabus",
      summary="Advanced fMRI analysis: efficient experimental design, brain connectivity and multi-voxel pattern analysis.", graphic="rail", demos=[]),
 dict(id="cambridge-cognitive-psychology", title="Introduction to Cognitive Psychology and Neuropsychology", provider="University of Cambridge · Coursera", tutors="Giulia Mangiaracina", status="cert", cert="cam_cog", url=CAM_COG_URL, outcomes=CAM_COG, kind="syllabus",
      summary="How human cognition is studied, and how memory, language, attention and perception work.", graphic="rail", demos=[]),
 dict(id="cambridge-neuropsychology-of-decision-making", title="The Neuropsychology of Decision Making", provider="University of Cambridge · Coursera", tutors="Stacey Bedwell", status="cert", cert="cam_dm", url=CAM_DM_URL, outcomes=CAM_DM, kind="syllabus",
      summary="How the prefrontal cortex, neurotransmitter systems and early experience shape the way people make decisions.", graphic="rail", demos=[]),
 dict(id="cambridge-psychology-of-emotions", title="The Psychology of Emotions: An Introduction to Embodied Cognition", provider="University of Cambridge · Coursera", tutors="Giulia Mangiaracina", status="cert", cert="cam_em", url=CAM_EM_URL, outcomes=CAM_EM, kind="syllabus",
      summary="A cognitive-psychology account of how emotions are felt in the body, studied experimentally and recognised in other people.", graphic="rail", demos=[]),
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
 "cam_cog": dict(major="psych", url=CAM_COG_URL, summary="How cognition is studied, and how memory, language, attention and perception work.",
                 skills=["Psychology", "Research Methodologies", "Learning Theory", "Human Learning", "Magnetic Resonance Imaging", "Research"]),
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
      lessons=['Introduction to deep learning and neural networks: neurons and neural networks, artificial neural networks, forward propagation', 'Basics of deep learning: gradient descent, backpropagation, vanishing gradient, activation functions', 'Keras and deep learning libraries: regression models and classification models with Keras', 'Deep learning models: shallow versus deep networks, convolutional networks, recurrent networks, transformers, autoencoders'],
      skills=["Deep Learning", "Keras", "Artificial Neural Networks", "Backpropagation", "Gradient Descent", "Convolutional Neural Networks", "Recurrent Neural Networks (RNNs)", "Autoencoders", "Artificial Intelligence", "Data Science"]),
 dict(title="PyTorch Basics for Machine Learning", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/pytorch/ibm-pytorch-basics-for-machine-learning", lessons_label="Modules",
      lessons=['Tensors: 1D and 2D tensors, differentiation in PyTorch, datasets', 'Linear regression: prediction, training, loss, gradient descent, cost', 'Linear regression the PyTorch way: stochastic and mini-batch gradient descent, optimisation, training, validation and test splits', 'Multiple input and output linear regression: prediction and training', 'Logistic regression for classification: linear classifiers, Bernoulli distribution and maximum likelihood, cross-entropy loss', 'Practice project: a neural network for breast cancer classification'],
      skills=["PyTorch", "Machine Learning", "Tensors", "Gradient Descent", "Linear Regression", "Logistic Regression", "Loss Functions", "Python Programming", "NumPy", "Pandas"]),
 dict(title="Deep Learning with Python and PyTorch", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-deep-learning-with-python-and-pytorch", lessons_label="Modules",
      lessons=['Logistic regression and cross-entropy loss', 'Softmax regression: multi-class classification', 'Shallow neural networks: hidden neurons, multi-dimensional input, multi-class networks, backpropagation, activation functions', 'Deep networks: dropout, weight initialisation, gradient descent with momentum, batch normalisation', 'Convolutional neural networks: convolution, max pooling, multiple channels, a CNN for MNIST, torchvision models, GPUs', 'Final project'],
      skills=["PyTorch", "Deep Learning", "Convolutional Neural Networks", "Artificial Neural Networks", "Backpropagation", "Autoencoders", "Transfer Learning", "Dimensionality Reduction", "Principal Component Analysis", "Python Programming"]),
 dict(title="Deep Learning with TensorFlow and Keras", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-deep-learning-with-tensorflow-and-keras", lessons_label="Modules",
      lessons=['Advanced Keras functionalities: functional and subclassing APIs, custom layers, TensorFlow 2.x', 'Advanced CNNs in Keras: data augmentation, transfer learning, pre-trained models, transpose convolution', 'Transformers in Keras: sequential data and time-series prediction', 'Unsupervised learning and generative models: autoencoders, diffusion models, generative adversarial networks', 'Advanced Keras techniques: custom training loops, hyperparameter tuning, model optimisation', 'Reinforcement learning: Q-learning and deep Q-networks', 'Final project'],
      skills=["TensorFlow", "Keras", "Convolutional Neural Networks", "Transformer Models", "Time Series", "Reinforcement Learning", "Unsupervised Learning", "Transfer Learning", "Autoencoders", "Deep Learning"]),
 dict(title="Applied Deep Learning Capstone Project", provider=IBM, major="ml", page=None, url="https://www.edx.org/learn/deep-learning/ibm-applied-deep-learning-capstone-project", lessons_label="Modules",
      lessons=['Data handling: memory-based versus generator-based loading, augmentation in Keras and PyTorch', 'CNN model development: building a CNN classifier', 'Integrating a CNN with a vision transformer', 'Final project submission'],
      skills=["Deep Learning", "PyTorch", "Keras", "Image Classification", "Model Evaluation", "Data Preprocessing"]),
]

# ---- toolkit, for the home page. (name, colour, "used" in my own projects | "course" for audited coursework only)
TOOLKIT = [
 ("Languages", [("Python", "#3776AB", "used"), ("R", "#276DC3", "used"), ("Bash", "#3E8E2C", "used"), ("C", "#5C6BC0", "used"), ("C++", "#00599C", "used"), ("HTML", "#C8532B", "used"), ("DBMS", "#336791", "used")]),
 ("Data and statistics", [("pandas", "#3B2A8C", "used"), ("NumPy", "#4D77CF", "used"), ("SciPy", "#0054A6", "used"), ("statsmodels", "#3F4F75", "used"),
                          ("tidyverse", "#2C3E66", "used"), ("ggplot2", "#4F7CAC", "used"), ("vegan", "#4E7D2B", "used")]),
 ("Machine learning", [("scikit-learn", "#C96A00", "used"), ("PyTorch", "#EE4C2C", "used"), ("Keras", "#D00000", "course"), ("TensorFlow", "#E65C00", "course")]),
 ("Omics", [("Scanpy", "#6A4C93", "used"), ("Squidpy", "#8A3F7C", "used"), ("AnnData", "#2F7D7B", "used"), ("GSEApy", "#8D5A2B", "used"),
            ("Biopython", "#3A7CA5", "used"), ("MaAsLin3", "#7A5C00", "used"), ("MetaPhlAn", "#A8326A", "used"), ("HUMAnN", "#8D2C2C", "used")]),
 ("Workflow", [("Linux", "#B8860B", "used"), ("Git", "#D9411E", "used"), ("Jupyter", "#C75B12", "used"), ("Docker", "#1D7FC4", "used"), ("Nextflow", "#1E9E73", "used"), ("Snakemake", "#03627A", "used"), ("pytest", "#0A7FB0", "used")]),
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
  dict(key="ad", name="Alzheimer's disease and neurodegeneration", note="Research projects and a review, 2020 to 2026", link="alzheimers-project.html", projects_label="Projects and review",
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
              "yale": "neuro/psych", "cam_cog": "neuro/psych", "cam_em": "neuro/psych", "cam_dm": "neuro/psych", "ph125": "dl/ml",
              "gentech": "bioinf/courses", "pygen": "bioinf/courses", "galaxy": "bioinf/courses", "dnaseq": "bioinf/courses", "bigdata": "bioinf/courses", "gut": "bioinf/courses", "covid": "bioinf/courses",
              "biotech": "biotech/applied", "drug": "biotech/applied", "stem": "biotech/applied", "permed": "biotech/applied"}
AUDIT_GROUP = ["neuro/fund", "neuro/fund", "neuro/fund", "neuro/comp", "dl/keras", "dl/pytorch", "dl/pytorch", "dl/keras", "dl/pytorch"]
# Module names as listed on the course pages
CERT_MODULES = {
 "uw": ["Introduction and basic neurobiology", "Neural encoding models", "Neural decoding", "Information theory and neural coding", "Computing in carbon", "Computing with networks", "Plasticity in the brain and learning", "Learning from supervision and rewards"],
 "uchicago": [o[2] for o in UCHICAGO], "yale": [o[2] for o in YALE], "cam_dm": [o[2] for o in CAM_DM], "cam_cog": [o[2] for o in CAM_COG], "cam_em": [o[2] for o in CAM_EM],
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

# ---- detailed course content, shown inside the learning outcomes on course pages.
# course id -> {outcome text: (one-line description, [lecture topics])}. Topics follow the lecture titles on the course page.
COURSE_DETAIL = {
 "uchicago-understanding-the-brain": {
  "The nervous system": ("The four functions of the nervous system, its cells and coverings, and what goes wrong in tumours and demyelinating disease.",
   ["The four functions", "Central anatomy", "Neurons and their parts", "Neuronal diversity", "Glial cells", "Myelin", "Demyelinating diseases", "Meninges", "Peripheral diseases", "Brain tumours", "The brain and the spinal cord"]),
  "Neural communication and embodied emotion": ("How neurons signal electrically and chemically, and how the autonomic and enteric systems tie emotion to the body.",
   ["Electrical signalling", "Action potential", "Neurotransmitter synthesis and release", "Clostridial toxins", "Signal termination", "Receptors", "Metabotropic receptors", "Embodied emotion", "Enteric nervous system", "Sympathetic and parasympathetic balance", "Autonomic pharmacology", "Spinal cord injury"]),
  "Neuroanatomy": ("How the brain develops and is organised, its blood supply and major pathways, and how lesions map onto symptoms.",
   ["Neural tube formation and defects", "Brain vesicles", "Expansion of the cerebral cortex", "Forebrain tracts", "Cerebral palsy", "Nerves", "Regional and hemispheric functions", "Aphasia and language circuits", "Cerebral blood flow and blood supply", "Strokes, tumours and bleeds", "Spinal cord", "Telencephalon and cortex", "Cerebellum", "Visual pathway", "Pituitary tumours", "Hippocampus and Alzheimer's disease"]),
  "Perception and vision": ("How the brain interprets sensory input, and how the eye and the visual pathway build what we see.",
   ["Optical and auditory illusions", "Weber's law", "The visual pathway", "Distance and near vision", "Emmetropization", "Rods and cones", "Central and colour vision", "Visual fields", "The importance of edges", "Visual perception", "Learning to see", "Sheep brain dissection"]),
  "The vestibular sense and gaze": ("How the inner ear senses head movement and drives the reflexes and eye movements that keep gaze stable.",
   ["The vestibular stimulus", "Canals and otoconial masses", "Hair cell orientation", "Yoked end organs", "Otoconial disorders", "Visual integration", "The vestibulo-ocular reflex and its circuitry", "Nystagmus", "Adapting the reflex", "Saccades and their control"]),
  "Voluntary movements": ("How the motor system is organised, from motoneurons and muscle fibres to reflexes, posture and self-generated movement.",
   ["Motor hierarchy", "Fast and slow fibres", "Motoneuron types", "Orderly recruitment", "Monosynaptic reflex", "Co-activation", "Gamma reflex loop", "Postural control", "Central pattern generators", "Praxis", "Emotional movements"]),
  "Motor modulation": ("How the cerebellum and basal ganglia refine, select and learn movements, and what fails in Parkinson's disease.",
   ["The Purkinje cell", "Cerebellar functions, topography and laterality", "Efference copy and sensory reafference", "Cerebellar learning", "Action selection", "Basal ganglia anatomy and pathways", "Operational learning", "Chunking", "Parkinson's disease", "Non-motor functions of the basal ganglia"]),
  "Homeostasis": ("How the hypothalamus and brainstem keep temperature, breathing, urination and sleep within working limits.",
   ["Hypothalamic anatomy", "Pituitary gland", "Post-partum mood disorders", "Thermoregulation", "Hyperthermia, fever and hot flashes", "Breathing", "Urination", "Sleep phenomenology and mechanisms"]),
  "Abstract function": ("Emotion, attention, memory and language, and the disorders that reveal how they work.",
   ["Emotion", "Thalamic attention", "Memory types", "PTSD", "Semantic and episodic memory", "The story of H.M.", "Memory formation circuitry", "Amnesia", "Language and aphasias", "Prosody", "Intellectual disability"]),
 },
}

# Courses whose outcomes come from my own notes: the official modules are listed first. (module, description, lecture topics)
COURSE_MODULES = {
 "jhu-neuroimaging": [
  ("Structural neuroanatomy of the human brain", "The terminology of neuroscience and the structure, development and blood supply of the human brain.",
   ["Structure and anatomy", "Development of the brain", "Vascular organisation", "Terminology of brain organisation"]),
  ("Functional neuroanatomy of the human brain", "How neurons communicate, how function maps onto anatomy, and how cognition is organised and assessed.",
   ["Electrical and chemical communication in the brain", "Functional anatomy of the brain", "Organisation of cognitive domains", "Neuropsychological assessment of cognition"]),
  ("Principles and methods of neuroimaging", "The main approaches to imaging the brain, the basics of MRI and fMRI, and what structural and functional studies show.",
   ["Approaches to neuroimaging", "Basics of MRI", "Basics of fMRI", "Structural MRI studies", "Functional MRI studies"]),
  ("Experimental design and special applications in neuroimaging", "How functional imaging experiments are designed, and the methods beyond standard fMRI.",
   ["Experimental design", "Functional connectivity MRI", "Diffusion tensor imaging", "Magnetic resonance spectroscopy"]),
 ],
}

COURSE_DETAIL["yale-introduction-to-psychology"] = {
 "Foundations: neuroscience, Freud, Skinner": ("The physical basis of mental life, and the two theories that shaped modern psychology: Freud's psychodynamics and Skinner's behaviourism.",
  ["Dualism", "Neurons", "Parts of the brain", "The two hemispheres", "Freud and the psychodynamic approach", "Stages of development", "Defence mechanisms", "Scientific assessment of Freud", "Habituation", "Classical conditioning", "Instrumental conditioning", "Scientific assessment of Skinner"]),
 "Development and language": ("How infants and children think and how that is studied, then the structure of language, how it is learned and how it relates to thought.",
  ["Piaget's developmental stage theory", "Scientific evaluation of Piaget", "Methods for studying infants", "How children differ from adults", "Explanations for development", "Phonology", "Morphology", "Syntax", "Language acquisition", "Language and thought"]),
 "Cognition: perception, attention, memory": ("How we perceive the world, how attention works and how experience is stored in memory.",
  ["Problems of perception", "Perception of brightness, objects and depth", "Attention", "Memory distinctions", "Memory storage", "Learning and remembering", "Failures of memory", "False memories"]),
 "Self and others: emotion, social psychology": ("Social and non-social emotions and their evolution, and how people understand themselves and deal with others.",
  ["Evolution of emotion", "Facial expressions", "Fear", "Kinship", "Attachment", "Prisoner's dilemma", "Irrationality and culture", "The self", "Attribution", "Liking", "The psychology of groups", "Social categories"]),
 "Variation: personality, intelligence, mental illness, therapy": ("How and why people differ in personality and intelligence, followed by the major mental illnesses and their treatment.",
  ["Personality", "Intelligence", "Behavioural genetics", "Genes and environment", "Parenting", "Schizophrenia", "Mood disorders", "Anxiety disorders", "Dissociative disorders", "Personality disorders", "Therapy"]),
 "The good life: happiness": ("How psychologists measure happiness and what contributes to a good life.",
  ["Positive psychology", "What is happiness?", "The happiness set point", "Happiness is relative", "Skewed judgments of past events", "Humility and optimism"]),
}

COURSE_DETAIL["jhu-principles-of-fmri-1"] = {
 "Introduction to fMRI, data acquisition and reconstruction": ("What fMRI analysis aims to show, how psychological inferences are drawn from it, and how the scanner turns signal into an image.",
  ["Goals of fMRI analysis", "fMRI data structure", "Psychological inference", "MR physics", "Forming an image", "K-space"]),
 "The fMRI signal, experimental design and pre-processing": ("Where the BOLD signal comes from and what limits it, how experiments are designed, and how the data are cleaned before analysis.",
  ["Signal, noise and BOLD physiology", "fMRI artefacts and types of noise", "Spatial and temporal resolution of BOLD", "Experimental design", "Kinds of designs", "Pre-processing of fMRI data"]),
 "The General Linear Model": ("Building, estimating and testing the General Linear Model for fMRI time series.",
  ["The General Linear Model", "Applying the GLM to fMRI data", "Building GLM models", "Linear basis sets", "Filtering and nuisance covariates", "GLM estimation", "Autoregressive noise models", "Contrasts and t-tests"]),
 "Group-level analysis and the multiple comparison problem": ("Combining subjects in group analyses, and controlling false positives across thousands of voxels.",
  ["Group-level analysis", "The multiple comparison problem in fMRI", "Family-wise error correction", "False discovery rate correction", "Pitfalls in multiple comparisons"]),
}

COURSE_DETAIL["cambridge-cognitive-psychology"] = {
 "What is cognitive psychology? History and core debates": ("The ideas behind modern psychology and the debates at its centre.",
  ["Nature and nurture", "Brain, mind and behaviour", "Plasticity in the adult brain", "Modularity of mind"]),
 "How do we measure the mind? Research methods": ("The methods cognitive psychology relies on, from lesion studies to imaging and brain stimulation.",
  ["Neuropsychological lesion studies", "MRI and fMRI", "PET", "EEG and MEG", "Single-cell recordings", "TMS and tDCS"]),
 "The psychology of human language": ("How language is structured, processed and acquired.",
  ["Language development", "Theories of language acquisition", "Shared attention between parent and infant", "Phonology and morphology", "Semantics and syntax", "The Stroop test"]),
 "Memory, perception and cross-modal interactions": ("Working memory and its models, and how the senses, language and memory influence one another.",
  ["Working memory", "Phonological loop", "Visuo-spatial sketchpad", "Auditory perception", "Visual perception", "Cross-modal effects"]),
 "Attention, consciousness and free will": ("How attention shapes experience, what happens when it is impaired, and how it relates to consciousness and free will.",
  ["Attention", "Visual spatial neglect", "Attention and consciousness", "Change blindness", "Free will"]),
}
COURSE_DETAIL["cambridge-neuropsychology-of-decision-making"] = {
 "Introduction to neuroanatomy and neurodevelopment": ("The anatomy and development of the brain needed to follow the later modules.",
  ["Neuroanatomy", "Neurodevelopment"]),
 "The importance of the prefrontal cortex": ("What makes the prefrontal cortex distinctive in structure and function, and the evidence for its role in decisions.",
  ["Structure of the prefrontal cortex", "Higher-order processes", "Research evidence on decision making"]),
 "Neurotransmitters, neurophysiology and decision networks": ("The neurotransmitters behind a decision, how they act physiologically, and the networks that connect the regions involved.",
  ["Neurotransmitters", "Neurophysiology", "Brain connectivity", "Decision networks"]),
 "Decision making styles and the role of childhood experiences": ("Decision making as a process that develops: adult differences in style and the childhood factors that shape them.",
  ["Decision-making styles", "Development of decision making", "Childhood experiences"]),
 "Decision making deficits": ("Deficits in decision making, such as those seen in schizophrenia, with their biological causes and external factors.",
  ["Observed deficits", "Schizophrenia", "Biological causes", "External and childhood factors"]),
}

COURSE_DETAIL["jhu-principles-of-fmri-2"] = {
 "Psychological and behavioural inference, and advanced experimental design": ("What can and cannot be concluded from fMRI results, how meta-analysis sharpens inference, and how to match acquisition to the study's aims.",
  ["Reproducibility problems and solutions", "Circularity and reverse inference", "Meta-analysis", "Using meta-analysis to improve inference", "Optimising acquisition for the study goals", "Resting-state fMRI"]),
 "Advanced experimental design and advanced GLM modelling": ("Designing efficient experiments and building more robust models of the data.",
  ["Design efficiency", "Efficiency in fMRI", "Optimising designs with genetic algorithms", "Parametric modulators", "Basis sets", "Multicollinearity and diagnostics", "Robust regression", "Practical group analysis"]),
 "Brain connectivity": ("The different kinds of brain connectivity and the methods used to estimate them.",
  ["Types of brain connectivity", "Functional connectivity", "Multivariate decomposition methods", "Dynamic connectivity", "Graph theory and network analysis", "Effective connectivity", "Mediation, moderation and structural models"]),
 "Multi-voxel pattern analysis": ("Causal modelling of connectivity, then predicting mental states from patterns of activity across voxels.",
  ["Dynamic causal modelling", "Granger causality", "Principles of causal inference", "Multi-voxel pattern analysis", "Performing MVPA", "Worked example: a neural signature of pain"]),
}

COURSE_DETAIL["jhu-neurohacking-in-r"] = {
 "Introduction": ("What structural MRI data look like and why R is a workable tool for analysing them.",
  ["Structural MRI", "R for neuroimaging"]),
 "Neuroimaging: formats and visualization": ("The formats brain images come in, the common MRI scan types, and how to read, plot and manipulate them in R.",
  ["Data structures and operations", "The NIfTI format", "Basic visualisation", "Basic data manipulation", "Transformations and smoothing", "Basic MRI contrasts"]),
 "Image processing": ("The standard steps for preparing a brain MRI: inhomogeneity correction, brain extraction and registration.",
  ["Pre-processing overview", "Registration", "Bias field correction with fslr", "Brain extraction with fslr", "Image registration with fslr", "Data manipulation with ANTsR", "Pre-processing with ANTsR"]),
 "Extended image processing": ("Processing a multi-sequence scan end to end, registering to a template, segmenting tissue and exploring images interactively.",
  ["Co-registration with fslr and ANTsR", "Wrapper functions for processing pipelines", "Across-visit co-registration of T1 images", "Rigid, affine and nonlinear registration to a template", "Regional anatomy from nonlinear registration", "Tissue-level segmentation", "Interactive viewing with papayar"]),
}
COURSE_DETAIL["cambridge-psychology-of-emotions"] = {
 "What is cognitive psychology?": ("The main findings, theories and methods of cognitive psychology, which treats the mind as a processor of information.",
  ["Key findings and theories", "Research methods", "Perception, attention, language and memory", "Thinking and consciousness"]),
 "How we feel emotions": ("The core ideas of social cognition: how mirror neurons and theory of mind let us understand what others feel.",
  ["Emotional intelligence", "Embodied cognition", "Mirror neurons", "Theory of mind", "The importance of facial expression"]),
 "How do we study emotions?": ("The methods behind research on embodied emotion, including lesion studies, EEG and EMG.",
  ["Simulation theories", "Facial mimicry in the simulation process", "Neuropsychological lesion studies", "EEG and EMG"]),
 "How do we recognise others' emotional facial expressions?": ("The competing accounts of how facial expressions are recognised, and the evidence that mimicry helps.",
  ["Theory-theory and simulation models", "Neuroscience research methods", "Key EEG findings", "Key neuropsychological findings", "Key EMG findings"]),
 "Is it always easy to understand others' emotions?": ("What affects emotional understanding in real social situations: motivation, prior knowledge and ambiguous expressions.",
  ["Simulation in ambiguous contexts", "Simulation with ambiguous expressions", "Attitude and motivation towards the other person", "Prior knowledge"]),
}

COURSE_DETAIL["harvardx-mcb80-1x"] = {
 "Resting potential": ("Why a neuron at rest holds a voltage across its membrane, and how ion gradients and selective channels set its value.",
  ["The history of bioelectricity", "The resting potential", "The Nernst potential", "The GHK equation", "Ion filters", "Field trips: the Museum of Science and the human brain"]),
 "Passive membrane properties": ("How resistance and capacitance shape the way the membrane potential changes when current flows.",
  ["Changing the membrane potential", "Current and Ohm's law", "Resistance in the neuron", "Membrane capacitance", "Field trip: the Warren Anatomical Museum"]),
 "Action potentials": ("How the action potential is generated, phase by phase, and the ionic currents behind it.",
  ["Fundamentals of the action potential", "The phases of the action potential", "The currents behind the action potential", "Field trips: neurotoxins at the aquarium, and electroreception"]),
}

COURSE_DETAIL["harvardx-mcb80-2x"] = {
 "The synapse": ("How a signal crosses from one neuron to the next, and what happens in the presynaptic terminal.",
  ["The basics of synaptic transmission", "The presynaptic terminal", "Visualising the synapse"]),
 "Excitation and inhibition": ("How excitatory and inhibitory inputs move the membrane potential, and the diseases that follow when either is disturbed.",
  ["EPSPs and IPSPs", "Disease states of excitation", "Disease states of inhibition", "Field trip: the Tye Lab at MIT"]),
 "Small circuits": ("How a neuron combines its inputs in space and time, and how circuits are mapped.",
  ["Synaptic efficacy and distance", "Synaptic summation", "Synaptic inhibition", "Temporal summation", "Temporal inhibition", "Field trip: connectomics in the Lichtman Lab"]),
 "Neuromodulation": ("How neuromodulators change the way circuits respond, through receptor types and the serotonin and dopamine systems.",
  ["What neuromodulation is", "Ionotropic receptors", "Metabotropic receptors", "The serotonin system", "The dopamine system", "The science of addiction"]),
 "Potentiation and depression": ("How synapses strengthen and weaken with use, the basis of learning.",
  ["Introduction to plasticity", "Short-term plasticity and adaptation", "Hebb's rule and associative learning", "Nonsynaptic plasticity", "MDMA-assisted psychotherapy"]),
}

COURSE_DETAIL["harvardx-mcb80-3x"] = {
 "Vision": ("How light is captured by the eye, processed in the retina and carried through the visual pathways of the brain.",
  ["The nature of light", "How the retina processes light", "Visual pathways in the brain", "Anatomy of the eye"]),
 "Audition": ("How sound is turned into neural signals and processed from the ear to the auditory cortex, and how hearing is lost.",
  ["The nature of sound", "Auditory anatomy", "Subcortical auditory processing", "The auditory cortex", "Conduction deafness", "Sensorineural hearing loss"]),
 "Touch, taste, smell and the remaining senses": ("The chemical senses and body sensation, and senses that other animals have and humans lack.",
  ["Gustation", "Olfaction", "Somatosensation", "Senses beyond the human range"]),
 "Movement and action": ("How muscles, motor neurons and reflexes produce movement, and what brain damage does to it.",
  ["Muscles", "Lower motor neurons", "Upper motor neurons", "Reflexes", "How brain damage affects movement", "Voluntary and reflex movements"]),
 "Subcortical brain areas": ("The structures beneath the cortex and what each contributes.",
  ["Hindbrain", "Midbrain", "Cerebellum", "Forebrain", "Limbic system"]),
}

COURSE_DETAIL["harvardx-mcb80-1x"].update({
 "Action potential propagation": ("How an action potential travels along the axon, and how axon size and myelin make it faster.",
  ["Signals in the nervous system", "Electrical signalling", "Getting from point A to point B", "Speeding up the action potential", "Giant axons", "Myelination in depth", "Field trip: sheep brain dissection"]),
 "DIY labs": ("Optional do-it-yourself experiments for recording and stimulating real neurons at home.",
  ["Recording and stimulating a nerve", "Rate coding", "Electrode referencing", "Neuropharmacology", "The electromyograph", "Grasshopper vision"]),
})

COURSE_MODULES["uw-computational-neuroscience"] = [
 ("Introduction and basic neurobiology", "What computational neuroscience is, and the neurobiology it rests on.",
  ["Descriptive models", "Mechanistic and interpretive models", "The electrical personality of neurons", "Synapses", "Brain areas and their function"]),
 ("What do neurons encode? Neural encoding models", "How a neuron's response can be modelled from the stimulus that drives it.",
  ["The neural code", "Simple encoding models", "Feature selection", "Variability", "Convolutions and linear systems", "Change of basis and PCA", "Eigenvectors and eigenvalues"]),
 ("Extracting information from neurons: neural decoding", "How to read a stimulus or decision back out of neural activity.",
  ["Signal detection theory", "Population coding and Bayesian estimation", "Stimulus reconstruction", "Visual processing in the retina (guest lecture)", "Gaussians and Bayes' rule"]),
 ("Information theory and neural coding", "How much information spike trains carry, and what makes a code efficient.",
  ["Information and entropy", "Calculating information in spike trains", "Coding principles"]),
 ("Computing in carbon", "Biophysical and simplified models of single neurons.",
  ["Modelling neurons", "Spikes", "Simplified model neurons", "Dendrites", "Neural correlations and synchrony (guest lecture)", "Dynamical systems: fixed points and nullclines"]),
 ("Computing with networks", "How connected neurons compute, from synapse models to recurrent networks.",
  ["Modelling connections between neurons", "Network models", "Recurrent networks"]),
 ("Networks that learn: plasticity in the brain and learning", "How synapses change with experience, and what networks learn without supervision.",
  ["Synaptic plasticity and Hebb's rule", "Statistical learning", "Unsupervised learning", "Sparse coding and predictive coding", "Gradient ascent and descent"]),
 ("Learning from supervision and rewards", "Neurons as classifiers, and learning from reward.",
  ["Supervised learning", "Reinforcement learning: predicting rewards", "Reinforcement learning: choosing actions", "Bidirectional brain-computer interfaces (guest lecture)"]),
]

COURSE_DETAIL["epflx-neuronal-dynamics-of-cognition"] = {
 "Associative memory and the Hopfield model": ("How a network of neurons can store patterns and recall them from partial cues.",
  ["Classification by similarity", "Detour on magnetic materials", "The Hopfield model", "Learning of associations", "Storage capacity"]),
 "Attractor networks and spiking neurons": ("Memories as stable states of network activity, and how the idea carries over to realistic spiking neurons.",
  ["Attractor networks", "The stochastic Hopfield model", "Energy landscape", "Low-activity patterns", "Spiking neurons"]),
 "Neuronal populations and mean-field theory": ("Describing thousands of neurons by the activity of the population they form.",
  ["Population activity", "Cortical populations", "Connectivity", "The mean-field argument", "Stationary mean-field", "Random networks"]),
 "Perception and cortical field models": ("Continuous models of cortex and the activity patterns they produce, applied to perception.",
  ["Transients", "Spatial continuum models of cortex", "Solution types", "Perception", "Head direction cells"]),
 "Decision making and competitive dynamics": ("Decisions as a competition between neuronal populations.",
  ["Perceptual decision making", "Theory of decision dynamics", "Solutions", "Simulations and experiments", "Decisions, actions and volition"]),
 "Synaptic plasticity and learning": ("Models of how synapses change, from short-term effects to spike-timing rules and memory formation.",
  ["Classification of plasticity", "Short-term plasticity", "Long-term plasticity", "Spike-timing models of plasticity", "From spiking models to rate models", "The triplet STDP model", "Online learning of memories"]),
}

AUDIT_SUMMARY = {
 "Deep Learning Fundamentals with Keras": "The building blocks of neural networks and how they are trained, with first models in Keras.",
 "PyTorch Basics for Machine Learning": "Tensors, automatic differentiation and regression models in PyTorch.",
 "Deep Learning with Python and PyTorch": "Shallow, deep and convolutional networks, built and trained in PyTorch.",
 "Deep Learning with TensorFlow and Keras": "Advanced Keras: CNNs, transformers, generative models and reinforcement learning.",
 "Applied Deep Learning Capstone Project": "An end-to-end image classification project that combines a CNN with a vision transformer.",
}

# ---- detailed content for the other (non-neuroscience) certified courses: cert key -> [(module, description, topics)]
OTHER_DETAIL = {
 "dnaseq": [
  ("DNA sequencing, strings and matching", "How sequencers produce reads, how DNA is handled as strings in Python, and the simplest way to match a read to a genome.",
   ["DNA sequencing past and present", "Genomes as strings, reads as substrings", "Manipulating DNA strings", "FASTQ format and base qualities", "Read alignment", "Naive exact matching"]),
  ("Preprocessing, indexing and approximate matching", "Faster matching through preprocessing and indexes, and matching that tolerates differences.",
   ["Boyer-Moore", "Repetitive elements", "k-mer indexes", "Hash tables and ordered structures", "Hamming and edit distance", "The pigeonhole principle"]),
  ("Edit distance, assembly, overlaps", "Dynamic programming for alignment, then the first steps of assembling a genome from reads.",
   ["Dynamic programming for edit distance", "Global and local alignment", "The laws of assembly", "Overlap graphs", "Finding all overlaps"]),
  ("Algorithms for assembly", "How assemblers build genomes, and why repeats make it hard.",
   ["Shortest common superstring", "Greedy assembly", "Repeats", "De Bruijn graphs and Eulerian walks", "Assemblers in practice", "Long reads"])],
 "bigdata": [
  ("Genes and data", "The molecular biology behind gene-expression data, and a first look at large cancer datasets.",
   ["DNA and genes", "RNA and proteins", "Transcription and translation", "Variables and big datasets", "cBioPortal"]),
  ("Preparing datasets for analysis", "Cleaning and shaping data before analysis, with an introduction to R.",
   ["Data sources", "Missing values", "Normalisation", "Discretisation", "Feature selection", "Sampling", "R and Jupyter notebooks"]),
  ("Finding differentially expressed genes", "Selecting the genes that differ between groups.",
   ["Filter methods", "Wrapper methods", "Evaluation schemes", "Heatmaps", "R scripts for feature selection"]),
  ("Predicting diseases from genes", "Classifiers that predict disease from expression profiles.",
   ["Nearest-neighbour and rule-based methods", "Neural networks", "Statistical and probabilistic classifiers", "Evaluation schemes", "Prediction workflow"]),
  ("Determining gene alterations", "Mutations, methylation and copy number changes, and how they relate to expression.",
   ["Genetic mutations", "Methylation", "Copy number alterations", "Alterations and gene expression"]),
  ("Clustering and pathway analysis", "Grouping genes and samples, and reading results at the level of pathways.",
   ["Similarity assessment", "k-means", "Density-based clustering", "Hierarchical clustering", "Pathway analysis and visualisation"])],
 "pygen": [
  ("Overview of Python and first steps", "What Python is and how to write and run a first program.", ["Overview of Python", "First steps toward programming"]),
  ("Data structures, ifs and loops", "Holding sequence data in Python and controlling what a program does with it.", ["Data structures", "Conditionals", "Loops"]),
  ("Functions, modules and packages", "Writing reusable code and organising it.", ["Functions", "Modules and packages"]),
  ("Reading and writing data, and Biopython", "Getting sequence data in and out of a program, and using Biopython for common tasks.", ["Files and user input", "Communicating with other programs", "Biopython"])],
 "gentech": [
  ("Overview", "What genomics and genomic data science are, with the cell and molecular biology they need.",
   ["Genomics", "Genomic data science", "Cell biology", "Molecules of molecular biology", "The Human Genome Project", "From genes to phenotypes"]),
  ("Measurement technology", "How DNA is amplified and sequenced.", ["Polymerase chain reaction", "Next-generation sequencing", "Applications of sequencing"]),
  ("Computing technology", "The computer science behind genomic software.", ["Algorithms", "Memory and data structures", "Efficiency", "Software engineering", "Computational biology software"]),
  ("Data science technology", "The statistics needed to trust a genomic result.",
   ["The central dogma of statistics", "Plotting data", "Sample size and variability", "Statistical significance", "Multiple testing", "Study design, batch effects and confounding"])],
 "gut": [
  ("Introduction to microbes and the human microbiome", "What microbes are and where the human microbiome comes from.", ["Microbes", "The human microbiome", "Where our microbes come from"]),
  ("Studying the microbiome", "The sequencing and omics methods used to study microbial communities.", ["The history of studying microbes", "High-throughput DNA sequencing", "Omics technologies"]),
  ("Making sense out of microbial data", "Identifying microbes and comparing communities.", ["Identifying a microbe", "Alpha-diversity", "Beta-diversity", "Visualising differences with QIIME"]),
  ("The human gut microbiome and your health", "How diet, age and disease shape the gut community, and how it can be changed.", ["Diet and age", "Obesity", "Gut disease", "Faecal transplants"]),
  ("Gut microbe-host interactions: beyond nutrition", "How gut microbes interact with the immune and nervous systems.", ["The immune system", "Autoimmune diseases and allergies", "The gut and the brain", "Machine learning on microbiome data"]),
  ("What's in the American Gut", "A large citizen-science survey of gut microbiomes and what it found.", ["The American Gut Project", "Collecting samples", "Comparing populations"])],
 "permed": [
  ("Introduction to personalised medicine", "What personalised medicine is, and why the Nordic countries are well placed for it.", ["What personalised medicine is", "The Nordic perspective"]),
  ("Health information used in personalised medicine", "The patient data behind personalised medicine and how it is made usable.", ["Patient information", "Data cleaning and validation", "Disease trajectories from longitudinal data", "Digital tools for patient engagement"]),
  ("Biomarkers, genetics and omics", "How biomarkers are found and how genetic information is used in the clinic.", ["Biomarkers", "Omics approaches to biomarker discovery", "Genetic information in clinical medicine"]),
  ("Evidence and documentation for clinical efficacy", "How evidence for personalised treatments is generated and brought into practice.", ["Novel trial designs", "Legal and ethical evidence generation", "From research to clinical practice"]),
  ("Communication in personalised medicine", "Talking about screening and risk with patients and the public.", ["Screening for rare and common diseases", "Communicating risk", "Patient-centred care", "Living with a risk variant", "Media coverage"]),
  ("Ethical, legal and social aspects", "The ethical, legal and social questions personalised medicine raises.", ["Ethical concerns", "Legal regulation", "Social aspects", "The future"])],
 "biotech": [
  ("Enzymes, enzyme discovery and engineering", "How enzymes work, how new ones are found, and how they are improved.", ["How enzymes work", "Discovering enzymes", "Characterising catalytic activity", "Directed evolution", "Rational design of biocatalysts"]),
  ("Methods in systems and synthetic biology", "Designing, building and testing biological systems.", ["Synthetic biology", "Computational modelling and systems biology", "Genome synthesis and editing", "Engineering pathways", "Debugging with metabolomics"]),
  ("Biochemical and bioprocess engineering", "Turning a biological process into an industrial one.", ["Microbial fermentation and bioreactor design", "Biocatalysis", "Recovery and purification of small and large molecules", "Process economics and scale-up"]),
  ("Pharmaceuticals and fine chemicals", "Industrial examples of enzymes used to make drugs and fine chemicals.", ["Hydrolases", "Transaminases", "Aldolases", "Alcohol dehydrogenases", "Nitrile hydratases", "Amino acid oxidases"]),
  ("Case studies: bioenergy and biomaterials", "Biotechnology applied to energy and materials.", ["Sustainable bioenergy", "New routes to biofuels", "Membrane processes", "Enzymatic biofuel cells", "Biomaterials and biomanufacturing"]),
  ("Case studies: glycoscience and biotherapeutics", "Sugars in medicine, and how protein drugs are made.", ["Glycoscience", "Glycoscience in pharmaceuticals", "Biopharmaceuticals in the clinic", "Biopharmaceutical production"])],
 "stem": [
  ("Introduction to stem cells", "What stem cells are, how they differentiate and why they matter.", ["How stem cells differentiate", "The history of stem cells", "Why stem cells are important", "Stem cells in other organisms"]),
  ("Using stem cells to study disease", "Reprogrammed cells as models of human disease.", ["Reprogramming", "Genome editing for disease modelling", "Developing new cures"]),
  ("Using stem cells to treat disease", "Where stem-cell therapies stand, and common misconceptions.", ["Adult (somatic) stem cells", "Myths about stem-cell therapy"]),
  ("The bioethics of stem cell research and therapy", "The ethical questions raised by stem-cell research and treatment.", ["Bioethics of research", "Bioethics of therapy"])],
 "drug": [
  ("Pharmaceutical and biotechnology industry landscape", "How the pharmaceutical and biotechnology industries are organised and where they are heading.", ["The pharma and biotechnology landscape", "Key issues for pharma", "Global outlook", "Patient-centric drug discovery", "A new approach to R&D", "Innovation"]),
  ("Drug discovery: proteomics, genomics", "Using genomics and proteomics to find and validate drug targets.", []),
  ("Compound selection and preclinical studies", "Choosing candidate compounds and testing them before human trials.", []),
  ("Fragment-based drug discovery for protein kinases", "Building kinase inhibitors up from small fragments, and why it is difficult.", []),
  ("Key concepts in drug delivery", "Getting a drug to the right place in the body at the right dose.", [])],
}

# ---- Alzheimer's project page
AD_STEPS = [
 ("Quality control", "Per-cell and per-gene filtering, with the detection gap between the two sections documented up front."),
 ("Clustering and annotation", "Leiden clustering and marker-based cell-type annotation, tuned separately for each section."),
 ("Composition and identity", "How cell-type proportions shift, and whether each type still expresses its defining programme."),
 ("Spatial statistics", "Neighbourhood enrichment and Moran's I to test whether cell types and genes are spatially organised."),
 ("Spatial zoning", "A transcriptional pathology index divides the Alzheimer's section into AD-hot and preserved zones."),
 ("Differential expression", "Zone against zone, globally and within each cell type, with gene-set and transcription-factor activity."),
 ("Trajectory and noise", "Pseudotime along OPC to oligodendrocyte maturation, transcriptional noise, and an integrated disruption index."),
 ("Machine learning", "Cell-type classifiers tested with a random split, a spatial hold-out, and transfer between the two sections."),
 ("External validation", "Core oligodendrocyte findings checked against the independent SEA-AD atlas."),
]
AD_LIMITS = [
 "One tissue section per condition, so there is no biological replication.",
 "A detection gap between sections (median 28 against 69 genes per cell) confounds direct cross-section comparisons; the analysis is built to avoid depending on them.",
 "A targeted gene panel, not the whole transcriptome: tau (MAPT) is not measured, and the pathology index is a transcriptional proxy.",
 "Cell types are annotated from markers, not confirmed by a pathologist.",
 "The results are correlational; nothing here establishes cause or the order of events.",
]
AD_TOOLS = ["Python", "Scanpy", "Squidpy", "AnnData", "GSEApy", "scikit-learn", "Jupyter", "Docker"]
