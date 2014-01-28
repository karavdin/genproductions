import FWCore.ParameterSet.Config as cms                                                                                                              
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
 
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(1.459e-09), # pb
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=0         ! User defined processes',
            'MSUB(157)=1            !   gg->A0',
            # MSSM settings
            'IMSS(4)= 2     ! masses fixed by user',
            'RMSS(1)= 100.  ! M1',   
            'RMSS(2)= 200.  ! M2',   
            'RMSS(3)= 800.  ! Mg',   
            'RMSS(4)= 200.  ! mu',   
            'RMSS(5)= 30.   ! tan beta', 
            'RMSS(6)= 1000.  ! MS',
            'RMSS(7)= 1000.  ! MS',
            'RMSS(8)= 1000.  ! MS',
            'RMSS(9)= 1000.  ! MS',
            'RMSS(10)= 1000.  ! MS',
            'RMSS(11)= 1000.  ! MS',
            'RMSS(12)= 1000.  ! MS',
            'RMSS(13)= 1000.  ! MS',
            'RMSS(14)= 1000.  ! MS',
            'RMSS(15)= 2000.  ! Ab',
            'RMSS(16)= 2000.  ! At',
            'RMSS(17)= 2000.  ! Atau',
            # Higgs masses
            'PMAS(25,1)=125.   ! mh',
            'PMAS(36,1)=260.  ! mA',
            # Switch off / on desirable channels for A->Zh
            'MDME(420,1)=  0   !    d               dbar',
            'MDME(421,1)=  0   !    u               ubar',
            'MDME(422,1)=  0   !    s               sbar',
            'MDME(423,1)=  0   !    c               cbar',
            'MDME(424,1)=  0   !    b               bbar',
            'MDME(425,1)=  0   !    t               tbar',
            'MDME(426,1)=  0   !    b              bbar ',
            'MDME(427,1)=  0   !    t              tbar ',
            'MDME(428,1)=  0   !    e-              e+  ',
            'MDME(429,1)=  0   !    mu-             mu+ ',
            'MDME(430,1)=  0   !    tau-            tau+',
            'MDME(431,1)=  0   !    tau-           tau+ ',
            'MDME(432,1)=  0   !    g               g   ',
            'MDME(433,1)=  0   !    gamma           gamma',
            'MDME(434,1)=  0   !    gamma           Z0',
            'MDME(435,1)=  0   !    Z0              Z0',
            'MDME(436,1)=  0   !    W+              W-',
            'MDME(437,1)=  1   !    Z0              h0 ',
            'MDME(438,1)=  0   !    h0              h0',
            'MDME(439,1)=  0   !    W+              H-',
            'MDME(440,1)=  0   !    H+              W-',
            'MDME(441,1)=  0   !    ~chi_10         ~chi_10',
            'MDME(442,1)=  0   !    ~chi_20         ~chi_10',
            'MDME(443,1)=  0   !    ~chi_20         ~chi_20',
            'MDME(444,1)=  0   !    ~chi_30         ~chi_10',
            'MDME(445,1)=  0   !    ~chi_30         ~chi_20',
            'MDME(446,1)=  0   !    ~chi_30         ~chi_30',
            'MDME(447,1)=  0   !    ~chi_40         ~chi_10',
            'MDME(448,1)=  0   !    ~chi_40         ~chi_20',
            'MDME(449,1)=  0   !    ~chi_40         ~chi_30',
            'MDME(450,1)=  0   !    ~chi_40         ~chi_40',
            'MDME(451,1)=  0   !    ~chi_1+         ~chi_1-',
            'MDME(452,1)=  0   !    ~chi_1+         ~chi_2-',
            'MDME(453,1)=  0   !    ~chi_2+         ~chi_1-',
            'MDME(454,1)=  0   !    ~chi_2+         ~chi_2-',
            'MDME(455,1)=  0   !    ~d_L            ~d_Lbar',
            'MDME(456,1)=  0   !    ~d_R            ~d_Rbar',
            'MDME(457,1)=  0   !    ~d_L            ~d_Rbar',
            'MDME(458,1)=  0   !    ~d_Lbar         ~d_R',
            'MDME(459,1)=  0   !    ~u_L            ~u_Lbar',
            'MDME(460,1)=  0   !    ~u_R            ~u_Rbar',
            'MDME(461,1)=  0   !    ~u_L            ~u_Rbar',
            'MDME(462,1)=  0   !    ~u_Lbar         ~u_R',
            'MDME(463,1)=  0   !    ~s_L            ~s_Lbar',
            'MDME(464,1)=  0   !    ~s_R            ~s_Rbar',
            'MDME(465,1)=  0   !    ~s_L            ~s_Rbar',
            'MDME(466,1)=  0   !    ~s_Lbar         ~s_R',
            'MDME(467,1)=  0   !    ~c_L            ~c_Lbar',
            'MDME(468,1)=  0   !    ~c_R            ~c_Rbar',
            'MDME(469,1)=  0   !    ~c_L            ~c_Rbar',
            'MDME(470,1)=  0   !    ~c_Lbar         ~c_R',
            'MDME(471,1)=  0   !    ~b_1            ~b_1bar',
            'MDME(472,1)=  0   !    ~b_2            ~b_2bar',
            'MDME(473,1)=  0   !    ~b_1            ~b_2bar',
            'MDME(474,1)=  0   !    ~b_1bar         ~b_2',
            'MDME(475,1)=  0   !    ~t_1            ~t_1bar',
            'MDME(476,1)=  0   !    ~t_2            ~t_2bar',
            'MDME(477,1)=  0   !    ~t_1            ~t_2bar',
            'MDME(478,1)=  0   !    ~t_1bar         ~t_2',
            'MDME(479,1)=  0   !    ~e_L-           ~e_L+',
            'MDME(480,1)=  0   !    ~e_R-           ~e_R+',
            'MDME(481,1)=  0   !    ~e_L-           ~e_R+',
            'MDME(482,1)=  0   !    ~e_L+           ~e_R-',
            'MDME(483,1)=  0   !    ~nu_eL          ~nu_eLbar',
            'MDME(484,1)=  0   !    ~nu_eR          ~nu_eRbar',
            'MDME(485,1)=  0   !    ~nu_eL          ~nu_eRbar',
            'MDME(486,1)=  0   !    ~nu_eLbar       ~nu_eR',
            'MDME(487,1)=  0   !    ~mu_L-          ~mu_L+',
            'MDME(488,1)=  0   !    ~mu_R-          ~mu_R+',
            'MDME(489,1)=  0   !    ~mu_L-          ~mu_R+',
            'MDME(490,1)=  0   !    ~mu_L+          ~mu_R-',
            'MDME(491,1)=  0   !    ~nu_muL         ~nu_muLbar',
            'MDME(492,1)=  0   !    ~nu_muR         ~nu_muRbar',
            'MDME(493,1)=  0   !    ~nu_muL         ~nu_muRbar',
            'MDME(494,1)=  0   !    ~nu_muLbar      ~nu_muR',
            'MDME(495,1)=  0   !    ~tau_1-         ~tau_1+',
            'MDME(496,1)=  0   !    ~tau_2-         ~tau_2+',
            'MDME(497,1)=  0   !    ~tau_1-         ~tau_2+',
            'MDME(498,1)=  0   !    ~tau_1+         ~tau_2-',
            'MDME(499,1)=  0   !    ~nu_tauL        ~nu_tauLbar',
            'MDME(500,1)=  0   !    ~nu_tauR        ~nu_tauRbar',
            'MDME(501,1)=  0   !    ~nu_tauL        ~nu_tauRbar',
            'MDME(502,1)=  0   !    ~nu_tauLbar     ~nu_tauR',            
             # Z->e+e- , mu+mu- , tau+tau-
            'MDME(174,1)=  0   !   d         dbar',
            'MDME(175,1)=  0   !   u         ubar',
            'MDME(176,1)=  0   !   s         sbar',
            'MDME(177,1)=  0   !   c         cbar',
            'MDME(178,1)=  0   !   b         bbar',
            'MDME(179,1)=  0   !   t         tbar',
            'MDME(180,1)=  0   !   b        bbar',
            'MDME(181,1)=  0   !   t        tbar',
            'MDME(182,1)=  1   !   e-        e+',
            'MDME(183,1)=  0   !   nu_e      nu_ebar',
            'MDME(184,1)=  1   !   mu-       mu+',
            'MDME(185,1)=  0   !   nu_mu     nu_mubar',
            'MDME(186,1)=  1   !   tau-      tau+',
            'MDME(187,1)=  0   !   nu_tau    nu_taubar',
            # h->b bbar
            'MDME(210,1)=  0   !    d               dbar ',   
            'MDME(211,1)=  0   !    u               ubar', 
            'MDME(212,1)=  0   !    s               sbar',    
            'MDME(213,1)=  0   !    c               cbar',    
            'MDME(214,1)=  1   !    b               bbar',    
            'MDME(215,1)=  0   !    t               tbar  ',  
            'MDME(216,1)=  0   !    b              bbar ',  
            'MDME(217,1)=  0   !    t              tbar ', 
            'MDME(218,1)=  0   !    e-              e+',      
            'MDME(219,1)=  0   !    mu-             mu+ ',    
            'MDME(220,1)=  0   !    tau-            tau+    ',
            'MDME(221,1)=  0   !    tau-           tau+   ',
            'MDME(222,1)=  0   !    g               g	    ',
            'MDME(223,1)=  0   !    gamma           gamma   ',
            'MDME(224,1)=  0   !    gamma           Z0	    ',
            'MDME(225,1)=  0   !    Z0              Z0	    ',
            'MDME(226,1)=  0   !    W+              W-	    ',
            'MDME(227,1)=  0   !    ~chi_10         ~chi_10', 
            'MDME(228,1)=  0   !    ~chi_20         ~chi_10 ',
            'MDME(229,1)=  0   !    ~chi_20         ~chi_20 ',
            'MDME(230,1)=  0   !    ~chi_30         ~chi_10 ',
            'MDME(231,1)=  0   !    ~chi_30         ~chi_20 ',
            'MDME(232,1)=  0   !    ~chi_30         ~chi_30 ',
            'MDME(233,1)=  0   !    ~chi_40         ~chi_10 ',
            'MDME(234,1)=  0   !    ~chi_40         ~chi_20 ',
            'MDME(235,1)=  0   !    ~chi_40         ~chi_30 ',
            'MDME(236,1)=  0   !    ~chi_40         ~chi_40 ',
            'MDME(237,1)=  0   !    ~chi_1+         ~chi_1- ',
            'MDME(238,1)=  0   !    ~chi_1+         ~chi_2- ',
            'MDME(239,1)=  0   !    ~chi_2+         ~chi_1- ',
            'MDME(240,1)=  0   !    ~chi_2+         ~chi_2- ',
            'MDME(241,1)=  0   !    ~d_L            ~d_Lbar ',
            'MDME(242,1)=  0   !    ~d_R            ~d_Rbar ',
            'MDME(243,1)=  0   !    ~d_L            ~d_Rbar ',
            'MDME(244,1)=  0   !    ~d_Lbar         ~d_R    ',
            'MDME(245,1)=  0   !    ~u_L            ~u_Lbar ',
            'MDME(246,1)=  0   !    ~u_R            ~u_Rbar ',
            'MDME(247,1)=  0   !    ~u_L            ~u_Rbar ',
            'MDME(248,1)=  0   !    ~u_Lbar         ~u_R    ',
            'MDME(249,1)=  0   !    ~s_L            ~s_Lbar ',
            'MDME(250,1)=  0   !    ~s_R            ~s_Rbar ',
            'MDME(251,1)=  0   !    ~s_L            ~s_Rbar ',
            'MDME(252,1)=  0   !    ~s_Lbar         ~s_R    ',
            'MDME(253,1)=  0   !    ~c_L            ~c_Lbar ',
            'MDME(254,1)=  0   !    ~c_R            ~c_Rbar ',
            'MDME(255,1)=  0   !    ~c_L            ~c_Rbar ',
            'MDME(256,1)=  0   !    ~c_Lbar         ~c_R    ',
            'MDME(257,1)=  0   !    ~b_1            ~b_1bar ',
            'MDME(258,1)=  0   !    ~b_2            ~b_2bar ',
            'MDME(259,1)=  0   !    ~b_1            ~b_2bar ',
            'MDME(260,1)=  0   !    ~b_1bar         ~b_2    ',
            'MDME(261,1)=  0   !    ~t_1            ~t_1bar ',
            'MDME(262,1)=  0   !    ~t_2            ~t_2bar ',
            'MDME(263,1)=  0   !    ~t_1            ~t_2bar ',
            'MDME(264,1)=  0   !    ~t_1bar         ~t_2    ',
            'MDME(265,1)=  0   !    ~e_L-           ~e_L+   ',
            'MDME(266,1)=  0   !    ~e_R-           ~e_R+   ',
            'MDME(267,1)=  0   !    ~e_L-           ~e_R+   ',
            'MDME(268,1)=  0   !    ~e_L+           ~e_R-   ',
            'MDME(269,1)=  0   !    ~nu_eL          ~nu_eLbar ',   
            'MDME(270,1)=  0   !    ~nu_eR          ~nu_eRbar',	 
            'MDME(271,1)=  0   !    ~nu_eL          ~nu_eRbar',	 
            'MDME(272,1)=  0   !    ~nu_eLbar       ~nu_eR	 ',
            'MDME(273,1)=  0   !    ~mu_L-          ~mu_L+	 ',
            'MDME(274,1)=  0   !    ~mu_R-          ~mu_R+	 ',
            'MDME(275,1)=  0   !    ~mu_L-          ~mu_R+	 ',
            'MDME(276,1)=  0   !    ~mu_L+          ~mu_R-	 ',
            'MDME(277,1)=  0   !    ~nu_muL         ~nu_muLbar',	 
            'MDME(278,1)=  0   !    ~nu_muR         ~nu_muRbar',	 
            'MDME(279,1)=  0   !    ~nu_muL         ~nu_muRbar',	 
            'MDME(280,1)=  0   !    ~nu_muLbar      ~nu_muR	 ',
            'MDME(281,1)=  0   !    ~tau_1-         ~tau_1+	 ',
            'MDME(282,1)=  0   !    ~tau_2-         ~tau_2+	 ',
            'MDME(283,1)=  0   !    ~tau_1-         ~tau_2+	 ',
            'MDME(284,1)=  0   !    ~tau_1+         ~tau_2-	 ',
            'MDME(285,1)=  0   !    ~nu_tauL        ~nu_tauLbar',	 
            'MDME(286,1)=  0   !    ~nu_tauR        ~nu_tauRbar',	 
            'MDME(287,1)=  0   !    ~nu_tauL        ~nu_tauRbar',	 
            'MDME(288,1)=  0   !    ~nu_tauLbar     ~nu_tau'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


ProductionFilterSequence = cms.Sequence(generator)


