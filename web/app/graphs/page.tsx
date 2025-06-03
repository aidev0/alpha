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

export default function GraphPage() {
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