from behave import given, when, then

@given(u'I navigate to the search country page')
def nav(context):
    """ 
    Navigate to the search country page
    """
    context.browser.get('http://localhost:5000/search_country')

@when(u'I click on the country to link to the country detail')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('Albania').click()

@then(u'I should see the country detail page')
def details(context):
    """ 
    if successful, then we should be directed to the country detail page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/country_detail/2'
    assert 'Clean Fuel Adoption Values for Albania' in context.browser.page_source