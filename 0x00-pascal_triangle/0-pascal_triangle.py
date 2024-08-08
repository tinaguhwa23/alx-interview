def pascal_triangle(n):
        """
            Returns a list of lists representing Pascal's Triangle up to the nth row.
                """
                    if n <= 0:
                                return []

                                triangle = [[1]]  # Start with the first row

                                    for i in range(1, n):
                                                # Each row is based on the previous row
                                                        prev_row = triangle[-1]
                                                                # Start the row with 1
                                                                        row = [1]
                                                                                # Calculate the middle values of the row
                                                                                        for j in range(1, i):
                                                                                                        row.append(prev_row[j-1] + prev_row[j])
                                                                                                                # End the row with 1
                                                                                                                        row.append(1)
                                                                                                                                # Append the row to the triangle
                                                                                                                                        triangle.append(row)

                                                                                                                                            return triangle

