
![[WorkMan Layout.png]]

On [[Typing.com]], you can use this script to adjust the layout:

```js
(() => {
    const rows = document.querySelectorAll('.keyboard-row');

    // Desired layout
    const layout = {
        1: ['q','d','r','w','b','j','f','u','p',';','[',']','\\'],
        2: ['a','s','h','t','g','y','n','e','o','i',"'"],
        3: ['z','x','m','c','v','k','l',',','.','/']
    };

    // Extract visible key label
    function getKeyLabel(key) {
        const labels = [...key.querySelectorAll('.key-label')];

        for (const label of labels.reverse()) {
            const text = label.textContent.trim();
            if (text && text.length <= 2) {
                return text.toLowerCase();
            }
        }

        return null;
    }

    // Build map of ALL existing keys
    const allKeys = [...document.querySelectorAll('.keyboard-key')];
    const keyMap = {};

    allKeys.forEach(key => {
        const label = getKeyLabel(key);

        if (label) {
            keyMap[label] = key;
        }
    });

    // Rearrange rows
    [1, 2, 3].forEach(rowIndex => {
        const row = rows[rowIndex];

        // Preserve special keys
        const specials = [...row.children].filter(el => {
            const text = el.textContent.toLowerCase();
            return (
                text.includes('tab') ||
                text.includes('caps') ||
                text.includes('shift') ||
                text.includes('enter')
            );
        });

        row.innerHTML = '';

        // Left special key
        if (specials[0]) {
            row.appendChild(specials[0]);
        }

        // Add desired layout keys
        layout[rowIndex].forEach(char => {
            const key = keyMap[char];

            if (key) {
                row.appendChild(key);
            }
        });

        // Right special key
        if (specials[1]) {
            row.appendChild(specials[1]);
        }
    });
})();
```