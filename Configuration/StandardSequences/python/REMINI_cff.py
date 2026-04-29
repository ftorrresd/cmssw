import FWCore.ParameterSet.Config as cms

patAlgosToolsTask = cms.Task()

from PhysicsTools.PatAlgos.slimming.miniAODFromMiniAOD_tools import miniAODFromMiniAOD_customizeAllData as miniAOD_customizeAllData
from PhysicsTools.PatAlgos.slimming.miniAODFromMiniAOD_tools import miniAODFromMiniAOD_customizeAllMC as miniAOD_customizeAllMC


def fixMini2MiniMuonIDs(process):
    process.slimmedMuonsUpdated.recomputeSoftMuonMvaRun3 = cms.bool(True)
    process.slimmedMuonsUpdated.recomputeMuonBasicSelectors = cms.bool(True)
    return process

