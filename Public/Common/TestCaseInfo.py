class TestCaseInfo():
    """
    测试用例的信息
    """
    def __init__(self,id="",name="",
                 owner="",result="",
                 starttime="",endtime="",
                 secondsDuration="",errorinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.secondDuration = secondsDuration
        self.errorinfo = errorinfo