from tests.flow.flo import Flo

def test_yes_for_wanna_play():
    Flo.test('tests/flow/bank_one_roll_then_quit.sim.txt')