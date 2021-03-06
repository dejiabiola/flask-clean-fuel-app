Feature: Country detail
""" 
Confirm that we can browse the search country page
"""

Scenario: success for visiting country detail page
    Given I navigate to the search country page
    When I click on the country to link to the country detail 
    Then I should see the country detail page

