# py-html-kit

IDK I just want to write some bs code and made this

```python
def render_tasks():
    tasks = [
        "Learn the basics of VDOM",
        "Build a simple web page with it",
        "Add interactivity with JavaScript"
    ]

    html_doc = Html(
        lang="en",
        children=[
            Head(
                children=[
                    Meta(charset="UTF-8"),
                    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                    Title(children=[Text("To-Do List App")]),
                    Script(src="https://cdn.tailwindcss.com")
                ]
            ),
            Body(
                class_="bg-slate-900 text-slate-100 flex items-center justify-center min-h-screen font-sans",
                children=[
                    Main(
                        class_="container mx-auto p-8 max-w-2xl bg-slate-800 rounded-2xl shadow-lg",
                        children=[
                            Section(
                                class_="mb-6",
                                children=[
                                    H1(class_="text-4xl font-bold text-center text-sky-400", children=[Text("My To-Do List")])
                                ]
                            ),
                            Section(
                                class_="mb-6",
                                children=[
                                    Form(
                                        id="todo-form",
                                        class_="flex gap-4",
                                        children=[
                                            Input(
                                                type="text",
                                                id="todo-input",
                                                placeholder="Add a new task...",
                                                class_="flex-grow bg-slate-700 border border-slate-600 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-sky-500 transition-all",
                                                required=True
                                            ),
                                            Button(
                                                type="submit",
                                                class_="bg-sky-500 hover:bg-sky-600 text-white font-bold py-2 px-6 rounded-lg text-lg transition-colors",
                                                children=[Text("Add")]
                                            )
                                        ]
                                    )
                                ]
                            ),
                            Section(
                                children=[
                                    Ul(
                                        id="todo-list",
                                        class_="space-y-3",
                                        children=[
                                            Li(
                                                class_="bg-slate-700 p-4 rounded-lg text-lg flex justify-between items-center transition-all",
                                                children=[
                                                    Span(children=[Text(task)]),
                                                    Button(
                                                        class_="remove-btn bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-3 rounded-lg text-sm transition-colors",
                                                        children=[Text("Remove")]
                                                    )
                                                ]
                                            ) for task in tasks
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    Script(children=[Text(
                        """
                        document.addEventListener('DOMContentLoaded', () => {
                            const form = document.getElementById('todo-form');
                            const input = document.getElementById('todo-input');
                            const list = document.getElementById('todo-list');

                            // --- Add Task Logic ---
                            form.addEventListener('submit', (event) => {
                                event.preventDefault();
                                const taskText = input.value.trim();
                                if (taskText !== '') {
                                    const newListItem = document.createElement('li');
                                    newListItem.className = 'bg-slate-700 p-4 rounded-lg text-lg flex justify-between items-center transition-all';

                                    // Use innerHTML to easily create the content with the remove button
                                    newListItem.innerHTML = `
                                        <span>${taskText}</span>
                                        <button class="remove-btn bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-3 rounded-lg text-sm transition-colors">Remove</button>
                                    `;

                                    list.appendChild(newListItem);
                                    input.value = '';
                                    input.focus();
                                }
                            });

                            // --- Remove Task Logic (Event Delegation) ---
                            list.addEventListener('click', (event) => {
                                if (event.target.classList.contains('remove-btn')) {
                                    const listItem = event.target.closest('li');
                                    listItem.remove();
                                }
                            });
                        });
                        """
                    )])
                ]
            )
        ]
    )

    return html_doc.render()
```
