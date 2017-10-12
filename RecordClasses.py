class LevelRecord:
    ## This class stores all of the data that is extracted for a given level record

    ## The initialization arguments are the outputs of levelExtract
    def __init__(self,isoName,energy,jpi,uncert,hlife,dhlife):
        self.isotope = isoName
        self.energy = energy
        self.jpi = jpi
        self.energy_uncert = uncert
        self.hlife = hlife
        self.hlife_uncert = dhlife

        self.ionization = '0+'

    def print_record(self):
        print('%s: %s, %s, %s, %s, %s' % (self.isotope,self.energy, self.jpi, self.energy_uncert, self.hlife, self.hlife_uncert)) 

    ## make_data_string must be defined for all record classes
    ## converts data to a string that can be written to file
    def make_data_string(self):
        exportValues = [self.isotope, self.energy, self.jpi, self.energy_uncert, self.hlife, self.hlife_uncert, self.ionization]
        dataString = ";".join([str(val) for val in exportValues])+'\n'
        return(dataString)
