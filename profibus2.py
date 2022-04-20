def doStartup(self):
    # Import the PROFIBUS hardware access modules
    # and keep references to it.
    try:
        import pyprofibus
        import pyprofibus.phy_serial, pyprofibus.phy_dummy
        self.pyprofibus = pyprofibus
    except (ImportError, RuntimeError) as e:
        self.raiseException("Failed to import PROFIBUS protocol stack "
            "module 'pyprofibus':\n%s" % str(e))

    # Initialize the DPM
    self.phy = None
    self.master = None
    try:
        self.__conf = self.pyprofibus.PbConf.fromFile(
                self.getParamValueByName("config"))

        phyType = self.__conf.phyType.lower().strip()
        if phyType == "serial":
            self.phy = self.pyprofibus.phy_serial.CpPhySerial(
                    debug=(self.__conf.debug >= 2),
                    port=self.__conf.phyDev)
        elif phyType == "dummy_slave":
            self.phy = self.pyprofibus.phy_dummy.CpPhyDummySlave(
                    debug=(self.__conf.debug >= 2))
        else:
            self.raiseException("Invalid phyType parameter value")
        self.phy.setConfig(baudrate=self.__conf.phyBaud)

        if self.__conf.dpMasterClass == 1:
            DPM_cls = self.pyprofibus.DPM1
        else:
            DPM_cls = self.pyprofibus.DPM2
        self.master = DPM_cls(phy=self.phy,
                      masterAddr=self.__conf.dpMasterAddr,
                      debug=(self.__conf.debug >= 1))

        self.__setupSlaves()
        self.master.initialize()

        self.slaveList = self.master.getSlaveList()
        self.cachedInputs = [None] * len(self.slaveList)

    except self.pyprofibus.PhyError as e:
        self.raiseException("Profibus-PHY error: %s" % str(e))
        self.__cleanup()
    except self.pyprofibus.DpError as e:
        self.raiseException("Profibus-DP error: %s" % str(e))
        self.__cleanup()
    except self.pyprofibus.FdlError as e:
        self.raiseException("Profibus-FDL error: %s" % str(e))
        self.__cleanup()
    except self.pyprofibus.conf.PbConfError as e:
        self.raiseException("Profibus configuration error: %s" % str(e))
        self.__cleanup()
