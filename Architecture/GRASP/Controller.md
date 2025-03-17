A class that stands in-between of User Interface and [[Use Case|Application Layer]], *orchestrating* information flow from UI into business logic code and vice versa, *separating* the two.

Changes to UI don't bother business code, and changes to the business code don't bother UI (leading to [[Protected Variations]] principle taking place).
