/* Habit template library: [area, name, icon, color, type, goal, schedule, part, extra] */
const TEMPLATES = (() => {
  const c = (kind, target, unit) => ({ kind, target, unit }), d = { kind: 'daily' };
  const L = [
    ['Health', 'Drink water', '\u{1F4A7}', '#0a84ff', 'build', c('count', 8, 'glasses'), d, 'anytime'],
    ['Health', 'Take vitamins', '\u{1F48A}', '#30d158', 'build', c('check'), d, 'morning'],
    ['Health', 'Eat fruit & veg', '\u{1F34E}', '#ff453a', 'build', c('count', 5, 'servings'), d, 'anytime'],
    ['Fitness', 'Workout', '\u{1F3CB}\uFE0F', '#ff9f0a', 'build', c('time', 30, 'min'), { kind: 'times', n: 4, per: 'week' }, 'evening'],
    ['Fitness', 'Walk 8,000 steps', '\u{1F45F}', '#ff9f0a', 'build', c('count', 8000, 'steps'), d, 'anytime'],
    ['Fitness', 'Run', '\u{1F3C3}', '#ff6b35', 'build', c('count', 3, 'km'), { kind: 'weekly', days: [1, 3, 5] }, 'morning'],
    ['Fitness', 'Stretch', '\u{1F938}', '#64d2ff', 'build', c('time', 10, 'min'), d, 'morning'],
    ['Learning', 'Study', '\u{1F4D6}', '#5e5ce6', 'build', c('time', 60, 'min'), { kind: 'weekly', days: [1, 2, 3, 4, 5] }, 'afternoon'],
    ['Learning', 'Practice a language', '\u{1F5E3}\uFE0F', '#5e5ce6', 'build', c('time', 15, 'min'), d, 'evening'],
    ['Learning', 'Practice a skill', '\u{1F3B8}', '#bf5af2', 'build', c('time', 20, 'min'), { kind: 'times', n: 3, per: 'week' }, 'evening'],
    ['Reading', 'Read', '\u{1F4DA}', '#ac8e68', 'build', c('count', 20, 'pages'), d, 'night'],
    ['Reading', 'Read a book a month', '\u{1F4D5}', '#ac8e68', 'build', c('check'), { kind: 'times', n: 1, per: 'month' }, 'anytime'],
    ['Productivity', 'Plan the day', '\u{1F4C5}', '#2f6bff', 'build', c('check'), d, 'morning'],
    ['Productivity', 'Deep work block', '\u{1F3AF}', '#2f6bff', 'build', c('time', 90, 'min'), { kind: 'weekly', days: [1, 2, 3, 4, 5] }, 'morning'],
    ['Productivity', 'Inbox zero', '\u{1F4E5}', '#64d2ff', 'build', c('check'), { kind: 'weekly', days: [1, 2, 3, 4, 5] }, 'afternoon'],
    ['Personal development', 'Journal', '\u{1F4D3}', '#bf5af2', 'build', c('check'), d, 'night'],
    ['Personal development', 'Learn something new', '\u{1F4A1}', '#ffd60a', 'build', c('check'), d, 'anytime'],
    ['Mindfulness', 'Meditate', '\u{1F9D8}', '#5e5ce6', 'build', c('time', 10, 'min'), d, 'morning'],
    ['Mindfulness', 'Gratitude', '\u{1F64F}', '#30d158', 'build', c('count', 3, 'things'), d, 'night'],
    ['Mindfulness', 'Breathe deeply', '\u{1F32C}\uFE0F', '#64d2ff', 'build', c('time', 5, 'min'), d, 'afternoon'],
    ['Organization', 'Tidy up', '\u{1F9F9}', '#ac8e68', 'build', c('time', 15, 'min'), d, 'evening'],
    ['Organization', 'Weekly review', '\u{1F5C2}\uFE0F', '#2f6bff', 'build', c('check'), { kind: 'weekly', days: [0] }, 'evening'],
    ['Organization', 'Pay bills', '\u{1F4B3}', '#30d158', 'build', c('check'), { kind: 'monthly', dom: 1 }, 'anytime'],
    ['Digital wellbeing', 'No phone in bed', '\u{1F4F5}', '#ff453a', 'quit', c('check'), d, 'night'],
    ['Digital wellbeing', 'Limit social media', '\u{1F4F1}', '#ff9f0a', 'reduce', { kind: 'check', limit: 2, unit: 'sessions' }, d, 'anytime'],
    ['Digital wellbeing', 'Screen-free hour', '\u{1F305}', '#30d158', 'build', c('time', 60, 'min'), d, 'evening'],
    ['Social connection', 'Call family or a friend', '\u{1F4DE}', '#ff375f', 'build', c('check'), { kind: 'times', n: 2, per: 'week' }, 'evening'],
    ['Social connection', 'Do a kind act', '\u{1F49B}', '#ffd60a', 'build', c('check'), d, 'anytime'],
    ['Sleep routines', 'Sleep by 11 PM', '\u{1F634}', '#5e5ce6', 'build', c('check'), d, 'night'],
    ['Sleep routines', 'Wake up early', '\u23F0', '#ff9f0a', 'build', c('check'), d, 'morning'],
    ['Creative activities', 'Draw or sketch', '\u{1F3A8}', '#bf5af2', 'build', c('time', 20, 'min'), { kind: 'times', n: 3, per: 'week' }, 'evening'],
    ['Creative activities', 'Write', '\u270D\uFE0F', '#ac8e68', 'build', c('count', 300, 'words'), d, 'morning'],
    ['Health', 'No sugar', '\u{1F36C}', '#ff453a', 'quit', c('check'), d, 'anytime'],
    ['Health', 'Quit smoking', '\u{1F6AD}', '#8e8e93', 'quit', c('check'), d, 'anytime'],
    ['Health', 'Fewer coffees', '\u2615', '#ac8e68', 'reduce', { kind: 'check', limit: 1, unit: 'cups' }, d, 'anytime'],
    ['Personal development', 'Morning routine', '\u{1F305}', '#ff9f0a', 'build', c('check'), d, 'morning', { check: ['Wake up', 'Make the bed', 'Morning hygiene', 'Review priorities', 'Start the first important task'] }],
    ['Sleep routines', 'Evening wind-down', '\u{1F319}', '#5e5ce6', 'build', c('check'), d, 'night', { check: ['Screens off', 'Prepare tomorrow', 'Read 10 pages', 'Lights out'] }]
  ];
  return L.map((x, i) => ({ id: 't' + i, area: x[0], name: x[1], icon: x[2], color: x[3], type: x[4], goal: x[5], sched: x[6], part: x[7], check: x[8] && x[8].check }));
})();
const AREA_TO_CAT = { Health: 'health', Fitness: 'fitness', Learning: 'learn', Reading: 'learn', Productivity: 'work', 'Personal development': 'mind', Mindfulness: 'mind', Organization: 'home', 'Digital wellbeing': 'mind', 'Social connection': 'health', 'Sleep routines': 'health', 'Creative activities': 'learn' };
