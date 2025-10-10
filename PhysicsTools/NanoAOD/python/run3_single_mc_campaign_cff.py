import FWCore.ParameterSet.Config as cms


def run3_single_mc_campaign(process):
    if hasattr(process, "NANOAODSIMoutput"):
        mod = process.NANOAODSIMoutput

        mod.pedantic_trigger_naming = cms.untracked.bool(True)

        mod.process_name_mapping = cms.untracked.PSet(
            HLT2022=cms.untracked.string("HLT2022"),
            HLT2023=cms.untracked.string("HLT2023"),
            HLT2024=cms.untracked.string("HLT2024"),
            HLT=cms.untracked.string("HLT2025"),
        )

    return process
