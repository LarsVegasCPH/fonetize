from fonetize import rewriter


def test_rewrite():
    string = "Boogie Woogie"
    result = rewriter.rewrite(string)
    assert result == "Bravo oscar oscar golf india echo Whiskey oscar oscar golf india echo"
