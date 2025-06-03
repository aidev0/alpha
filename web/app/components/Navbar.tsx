'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const pathname = usePathname();

  const isActive = (path: string) => pathname === path;

  const menuItems = [
    { name: 'Home', path: '/' },
    { name: 'Chats', path: '/chats' },
    { name: 'Graphs', path: '/graphs' },
    { name: 'Plans', path: '/plans' },
    { name: 'Flows', path: '/flows' },
  ];

  return (
    <div className="bg-white p-4">
      {/* Rest of the component code */}
    </div>
  );
} 