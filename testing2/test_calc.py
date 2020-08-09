class TestCalc():
    def test_add(self, start, getadddata):
        result = start.add(getadddata[0], getadddata[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == getadddata[2]

    def check_sub(self, start, getsubdata):
        result = start.sub(getsubdata[0], getsubdata[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == getsubdata[2]

    def test_mul(self, start, getmuldata):
        result = start.mul(getmuldata[0], getmuldata[1])
        if isinstance(result, float):
            result = round(result, 3)
        assert result == getmuldata[2]

    def check_div(self, start, getdivdata):
        result = start.div(getdivdata[0], getdivdata[1])
        if getdivdata[1] == 0:
            assert type(result) == type(getdivdata[2])
        else:
            if isinstance(result, float):
                result = round(result, 3)
            assert result == getdivdata[2]
