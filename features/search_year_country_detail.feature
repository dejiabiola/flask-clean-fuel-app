Feature: Search year to Country detail
""" 
Confirm that we can browse the search year page
"""

Scenario: success for visiting country detail page
    Given I navigate to the search year page
    When I click on the link to the country detail 
    Then I should see the country details page

