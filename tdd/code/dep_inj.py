from time import asctime


class Report(object):
    def report(self):
        return ("at %s everything fine" % asctime())


class ReportDep(object):
    def __init__(self, timefunc=asctime):
        self.timefunc = timefunc

    def report(self):
        return ("at %s everything fine" % self.timefunc())


def test_report():
    func = lambda: "now"
    assert ReportDep(func).report() == 'at now everything fine'
