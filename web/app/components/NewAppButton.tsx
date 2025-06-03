'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

export default function NewAppButton() {
  const router = useRouter();

  const handleNewApp = () => {
    // TODO: Implement new app creation flow
    console.log('Create new app');
  };

  return (
    <button
      onClick={handleNewApp}
      className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition-colors"
    >
      Create New App
    </button>
  );
} 