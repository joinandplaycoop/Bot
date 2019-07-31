

class Table(object):
         
    def __init__(self, *args):
         #data about the column.  (width, header name)
         self._columns : list[Col] = []
         #all row text including text from header
         self._rows : list[list[str]] = []
         self._rows.append(args)
         for arg in args:
            self._columns.append(Col(arg))
            

    def addRow(self, *args):
        if len(args) != len(self._columns):
            raise ValueError(f"Invalid # of columns. Expected {len(self._columns)} got {len(args)}")

        self._rows.append(args)

    def toString(self) -> str:
        tableContents : str = ""

        #create rows
        for rowIndex in range(len(self._rows)):
            columns = self._rows[rowIndex]
            rowContents : str = ""
            divider : str = ""

            #create columns
            for colIndex in range(len(columns)):
                cell = str(columns[colIndex])

                #set column width automatically if not defined
                width : int = self._columns[colIndex].width

                if width == 0 :
                    width = self._columns[colIndex].width = len(max(self._rows, key = lambda x: len(str(x[colIndex])))[colIndex])

                if rowIndex == 0:
                    #create header
                    rowContents = rowContents + f"| {cell: <{width}} "
                    divider = divider + f"| {'':-<{width}} "

                    #add to table contents
                    if colIndex + 1 == len(columns):
                        rowContents = rowContents + "| \n"
                        divider = divider + "| \n"
                        tableContents = tableContents + rowContents
                        tableContents = tableContents + divider
                else:
                    #create body
                    rowContents = rowContents + f"| {cell: <{width}} "

                    #add to table contents
                    if colIndex + 1 == len(columns):
                         rowContents = rowContents + "| \n"
                         tableContents = tableContents + rowContents

        return "```prolog\n" + tableContents + "```"

class Col:

    def __init__(self, header, width=0):
        self.header : str = header
        self.width : int = width