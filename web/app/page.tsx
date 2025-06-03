'use client';

import React, { useMemo, useEffect, useState } from 'react';
import ReactFlow, {
  Background,
  Controls,
  MarkerType,
  Node,
  Edge,
} from 'reactflow';
import 'reactflow/dist/style.css';
// @ts-ignore
import dagre from 'dagre';

const nodeWidth = 180;
const nodeHeight = 80;

const dagreGraph = new dagre.graphlib.Graph();
dagreGraph.setDefaultEdgeLabel(() => ({}));
dagreGraph.setGraph({ rankdir: 'LR', nodesep: 120, ranksep: 100 });

function Home() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-8">
            Alpha AI Development Platform
          </h1>
          
          <p className="text-xl text-gray-600 mb-12">
            Build, deploy, and run software automatically across 1000+ integrations.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div className="p-8 bg-white rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold mb-4">AI-Powered Development</h3>
              <p>Automatically generate and deploy code across multiple platforms</p>
            </div>
            <div className="p-8 bg-white rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Smart Agents</h3>
              <p>Autonomous functions that execute tasks and support workflows</p>
            </div>
            <div className="p-8 bg-white rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold mb-4">Universal Integration</h3>
              <p>Connect with 1000+ services and platforms seamlessly</p>
            </div>
          </div>

          <div className="space-x-4">
            <a 
              href="/graphs" 
              className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg"
            >
              View Graphs
            </a>
            <a 
              href="/chats" 
              className="inline-block bg-gray-600 hover:bg-gray-700 text-white font-bold py-3 px-8 rounded-lg"
            >
              Start Chat
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

function GraphPage() {
  const [graph, setGraph] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchGraph = async () => {
      try {
        const apiUrl = process.env.NEXT_PUBLIC_ALPHA_API_URL || 'http://localhost:8001';
        console.log('Fetching from:', `${apiUrl}/graphs`);
        
        const response = await fetch(`${apiUrl}/graphs`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}, url: ${response.url}`);
        }
        const data = await response.json();
        console.log('Received data:', data);
        
        if (!data.graphs || data.graphs.length === 0) {
          throw new Error('No graphs found in the response');
        }
        
        setGraph(data.graphs[0]);
      } catch (err) {
        console.error('Error fetching graph:', err);
        setError(err instanceof Error ? err.message : 'Failed to fetch graph');
      } finally {
        setLoading(false);
      }
    };

    fetchGraph();
  }, []);

  const nodes: Node[] = useMemo(() => {
    if (!graph) return [];

    graph.nodes.forEach((node: any) => {
      dagreGraph.setNode(node.app_id, { width: nodeWidth, height: nodeHeight });
    });

    graph.edges.forEach(([from, to]: [number, number]) => {
      dagreGraph.setEdge(graph.nodes[from].app_id, graph.nodes[to].app_id);
    });

    dagre.layout(dagreGraph);

    return graph.nodes.map((node: any) => {
      const { x, y } = dagreGraph.node(node.app_id);
      return {
        id: node.app_id,
        data: { label: node.label },
        position: { x: y, y: x },
        type: 'default',
      };
    });
  }, [graph]);

  const edges: Edge[] = useMemo(() => {
    if (!graph) return [];

    return graph.edges.map(([from, to]: [number, number], index: number) => ({
      id: `e${index}`,
      source: graph.nodes[from].app_id,
      target: graph.nodes[to].app_id,
      type: 'smoothstep',
      markerEnd: {
        type: MarkerType.ArrowClosed,
        color: '#000',
      },
      style: {
        stroke: '#222',
        strokeWidth: 2,
      },
    }));
  }, [graph]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!graph) return <div>No graph data available</div>;

  return (
    <div style={{ width: '100%', height: '90vh' }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}

export default Home;
