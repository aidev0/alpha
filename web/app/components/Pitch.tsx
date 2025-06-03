'use client';

import React from 'react';

export default function Pitch() {
  return (
    <div className="max-w-4xl mx-auto text-center py-16 px-4">
      <h1 className="text-4xl font-bold mb-8">
        Alpha: Your AI Development Platform
      </h1>
      <p className="text-xl mb-8">
        Build, deploy, and run software automatically across 1000+ integrations. 
        Alpha acts as your universal developer and operator for any app idea.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
        <div className="p-6 bg-white rounded-lg shadow-lg">
          <h3 className="text-xl font-semibold mb-4">AI-Powered Development</h3>
          <p>Automatically generate and deploy code across multiple platforms</p>
        </div>
        <div className="p-6 bg-white rounded-lg shadow-lg">
          <h3 className="text-xl font-semibold mb-4">Smart Agents</h3>
          <p>Autonomous functions that execute tasks and support workflows</p>
        </div>
        <div className="p-6 bg-white rounded-lg shadow-lg">
          <h3 className="text-xl font-semibold mb-4">Universal Integration</h3>
          <p>Connect with 1000+ services and platforms seamlessly</p>
        </div>
      </div>
    </div>
  );
} 