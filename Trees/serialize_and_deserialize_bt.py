class Codec:

    def serialize(self, root):
        self.code = []

        def func(root):
            if not root:
                self.code.append("null")
                return

            self.code.append(str(root.val))
            func(root.left)
            func(root.right)

        func(root)

        return ",".join(self.code)

    def deserialize(self, data):
        self.nodes = data.split(",")
        self.index = 0

        def build():

            if self.nodes[self.index] == "null":
                self.index += 1
                return None

            newnode = TreeNode(int(self.nodes[self.index]))
            self.index += 1

            newnode.left = build()
            newnode.right = build()

            return newnode

        return build()