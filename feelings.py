import sophiaDiscord
import sophiaIRC

def baseFeelingsChange(change):
	sophiaDiscord.setBaseFeelings(getBaseFeelings + change)
	sophiaIRC.setBaseFeelings(getBaseFeelings + change)

def auxFeelingsChange(change):
	sophiaDiscord.setBaseFeelings(getAuxFeelings + change)
	sophiaIRC.setBaseFeelings(getAuxFeelings + change)