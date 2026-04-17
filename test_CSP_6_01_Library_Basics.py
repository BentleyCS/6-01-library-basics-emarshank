import CSP_6_01_Library_Basics as hw

def test_process_expenses():
    assert hw.process_expenses([1, 2]) == [1.15, 2.30]

def test_analyze_scores():
    assert hw.analyze_scores([3,4,5]) == 5, 4

def test_sanitize_usernames():
    assert hw.sanitize_usernames(["The Long Road", "x X x ROSES SCREAMING x X x"]) == ["thelongroad", "xxxrosesscreamingxxx"]

def test_identify_outliers():
    assert hw.identify_outliers([1, 10, 101, 102, 103]) == [101, 102, 103]
    
def test_search_and_report():
    assert hw.search_and_report(["apple", "zygote", "banana","abacus"], "banana") == 3
    
# test_process_expenses()
# test_analyze_scores()
# test_sanitize_usernames()
# test_identify_outliers()
# test_search_and_report()
    
