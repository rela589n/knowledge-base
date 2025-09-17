**Controller** is a class that stands **in-between** of (User Interface and [[Use Case|Application Layer]]), *orchestrating* information flow from UI into business logic code and vice versa, *separating* the two.

Leads to [[Protected Variations]], since
  Changes to UI don't bother business code, 
and changes to the business code don't bother UI.
