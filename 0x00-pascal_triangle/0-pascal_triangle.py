def pascal_triangle(n):
        """
            Returns a list of lists representing Pascal's Triangle up to the nth row.
                """
                    if n <= 0:
                                return []

                                triangle = []  # Initialize an empty list to hold all rows of the triangle

                                    for i in range(n):
                                                # Start each row with 1
                                                        row = [1] * (i + 1)
                                                                
                                                                        # Fill in the interior values of the row (if i > 1)
                                                                                if i > 1:
                                                                                                for j in range(1, i):
                                                                                                                    # Each element is the sum of the two elements directly above it
                                                                                                                                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]

                                                                                                                                            # Append the completed row to the triangle
                                                                                                                                                    triangle.append(row)

                                                                                                                                                        return triangle

