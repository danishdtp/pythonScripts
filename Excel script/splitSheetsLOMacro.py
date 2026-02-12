import uno
from com.sun.star.beans import PropertyValue
import os
import re  # Importing regular expressions
from urllib.parse import unquote


def split_by_column_D():
    try:
        doc = XSCRIPTCONTEXT.getDocument()
    except Exception as e:
        print(f"Error accessing the document: {e}")
        return

    sheet = doc.CurrentController.ActiveSheet
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(True)

    # Load all data into a list
    data = cursor.getDataArray()
    if len(data) < 2:
        return  # Exit if sheet is empty

    header = data[0]
    rows = data[1:]

    # Index 3 corresponds to Column D
    col_index = 3

    categories = set(row[col_index] for row in rows if row[col_index] is not None)

    desktop = XSCRIPTCONTEXT.getDesktop()

    # Retrieve the directory of the current document
    document_url = doc.getURL()
    save_dir = (
        os.path.dirname(unquote((document_url.replace("file:///", "")))) + "/"
    )  # Get the directory part
    print(save_dir)

    for cat in categories:
        safe_name = str(cat).replace("/", "_").replace("\\", "_")

        # Remove decimals from numbers in the safe_name
        safe_name = re.sub(r"\.\d+", "", safe_name)  # Remove decimal points

        new_doc = desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, ())
        new_sheet = new_doc.getSheets().getByIndex(0)

        filtered_data = [header] + [row for row in rows if row[col_index] == cat]

        target_range = new_sheet.getCellRangeByPosition(
            0, 0, len(header) - 1, len(filtered_data) - 1
        )
        target_range.setDataArray(tuple(filtered_data))

        os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists
        file_path = f"file:///{unquote(save_dir)}{safe_name}.xlsx"

        try:
            new_doc.storeToURL(file_path, (PropertyValue("FilterName", 0, "calc8", 0),))
        finally:
            new_doc.close(True)


g_exportedScripts = (split_by_column_D,)
