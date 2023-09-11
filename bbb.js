
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('deviceSelect').addEventListener('change', function() {
        // Reset selections on device change
        document.getElementById('itemSelect').value = "";
        document.getElementById('subItemSelect').innerHTML = "";
        document.getElementById('currentSelectionContainer').innerHTML = "";
    });

    document.getElementById('itemSelect').addEventListener('change', function() {
        var itemValue = this.value;
        var subItemSelect = document.getElementById('subItemSelect');
        subItemSelect.innerHTML = "";

        if (itemValue) {
            if (itemValue === 'Gaming') {
                addSubItem('LowEnd');
                addSubItem('HighEnd');
            } else if (itemValue === 'Photography') {
                addSubItem('Low');
                addSubItem('Medium');
                addSubItem('High');
            } else {
                addSubItem('Optimal');
            }
        }

        function addSubItem(subItemValue) {
            var option = document.createElement('option');
            option.value = subItemValue;
            option.textContent = subItemValue;
            subItemSelect.appendChild(option);
        }
    });
});

function addSelection() {
    var currentSelectionContainer = document.getElementById('currentSelectionContainer');
    var item = document.getElementById('itemSelect').value;
    var subItem = document.getElementById('subItemSelect').value;

    if (item && subItem) {
        var selectionText = item + " " + subItem;

        // Check if the parent item is already in the current selection
        var existingSelections = currentSelectionContainer.querySelectorAll('.selection-item');
        var parentItemAlreadySelected = false;

        existingSelections.forEach(function(selection) {
            if (selection.textContent.includes(item)) {
                parentItemAlreadySelected = true;
            }
        });

        if (!parentItemAlreadySelected) {
            var selectionElement = document.createElement('div');
            selectionElement.className = 'selection-item';
            selectionElement.textContent = selectionText;

            var removeButton = document.createElement('span');
            removeButton.className = 'remove-button';
            removeButton.textContent = 'x';
            removeButton.addEventListener('click', function() {
                removeSelection(selectionElement);
            });

            selectionElement.appendChild(removeButton);
            currentSelectionContainer.appendChild(selectionElement);
        }

        // Reset selections
        document.getElementById('itemSelect').value = "";
        document.getElementById('subItemSelect').innerHTML = "";
    }
}

function removeSelection(selection) {
    var currentSelectionContainer = document.getElementById('currentSelectionContainer');
    currentSelectionContainer.removeChild(selection);
}