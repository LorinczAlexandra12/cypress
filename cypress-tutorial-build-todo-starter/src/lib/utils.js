export const filterTodos = (filter, todos) => filter
    ? todos.filter(todos => todos.isComplete === (filter === 'completed'))
    : todos