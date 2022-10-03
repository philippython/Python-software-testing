Feature: Test navigation pages 

Scenario: Homepage can go to Blog
    Given  I am on the Homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page