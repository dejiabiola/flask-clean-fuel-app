from behave import given, when, then

@given(u'I navigate to the search year page')
def nav(context):
    """ 
    Navigate to the search country page
    """
    context.browser.get('http://localhost:5000/search_year')

@when(u'I click on the link to the country detail')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('16').click()

@then(u'I should see the country details page')
def details(context):
    """ 
    if successful, then we should be directed to the country detail page
    """

    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/country_detail/16'
    assert 'Clean Fuel Adoption Values for Belgium' in context.browser.page_source