import React from 'react';
import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import { store } from './store/store';
import HomePage from './pages/HomePage';
import ToDo from './pages/ToDo';
//
// test('renders learn react link', () => {
//   const { getByText } = render(
//     <Provider store={store}>
//       <HomePage />
//       <ToDo />
//     </Provider>
//   );
//
//   expect(getByText(/learn/i)).toBeInTheDocument();
// });
