class Outer:
    def __init__(self):
        print("Outer class object creation...")

    class Inner:
        def __init__(self):
           print("Inner Oject creation")

        class InnerInner:
            def __init__(self_):
                print("Inner Inner object creation")

            def m1(self):
                print('Inner class method')

                 
Outer().Inner().InnerInner().m1()
