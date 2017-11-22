class LevelRecord(object):
    ## This class stores all of the data that is extracted for a given level record

    ## The initialization arguments are the outputs of levelExtract
    def __init__(self, isoName, energy, jpi, uncert, hlife, dhlife):
        self.isotope = isoName
        self.energy = energy
        self.jpi = jpi
        self.energy_uncert = uncert
        self.hlife = hlife
        self.hlife_uncert = dhlife
        self.gammarays = []

        self.ionization = '0+'
        ## self.exportAttributes are the instance attributes that will be written to file
        self.exportAttributes = ['isotope', 'energy', 'jpi', 'energy_uncert', 'hlife', 'hlife_uncert', 'ionization']

    def print_record(self):
        print('%s: %s, %s, %s, %s, %s' % (self.isotope,self.energy, self.jpi, self.energy_uncert, self.hlife, self.hlife_uncert)) 

    ## converts data to a string that can be written to file
    def make_data_string(self):
        exportValues = [getattr(self, atty) for atty in self.exportAttributes]
        dataString = ";".join([str(val) for val in exportValues])+'\n'
        return(dataString)


class DecayRecord(LevelRecord):
    ## This class is an extension of LevelRecord that also stores decay data

    def __init__(self, levelRec, betaI, betaI_uncert, ecI, ecI_uncert, totBranchI):
        LevelRecord.__init__(self, levelRec.isotope, levelRec.energy, levelRec.jpi, levelRec.energy_uncert, levelRec.hlife, levelRec.hlife_uncert)
        self.gammarays = levelRec.gammarays
        self.betaI = betaI
        self.betaI_uncert = betaI_uncert
        self.ecI = ecI
        self.ecI_uncert = ecI_uncert
        self.totBranchI = totBranchI

        self.exportAttributes.extend(['totBranchI'])

class GammaRecord(object):
    def __init__(self, name, energy, energy_uncert, pi, pi_uncert,mpol,mr,mr_uncert,cc,cc_uncert):
        self.isoName = name
        self.energy = energy
        self.energy_uncert = energy_uncert
        self.photonIntensity = pi
        self.photonIntensity_uncert = pi_uncert
        self.multipolarity = mpol
        self.mixingRatio = mr
        self.mixingRadio_uncert = mr_uncert
        self.conversionCoeff = cc
        self.conversionCoeff_uncert = cc_uncert

    def __repr__(self):
        return (self.energy)
